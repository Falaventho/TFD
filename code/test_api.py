from dataprocessor import DataProcessor
from outputgenerator import OutputGenerator, ReportType
from utils import Record, InterestType, CompoundingInterval
import pytest
import random


class TestDataProcessor:

    @pytest.fixture
    def csv_contents(self) -> str:
        with open("./csv files/example.csv", "r") as f:
            contents = f.read()
        return contents

    @pytest.fixture
    def data_processor(self) -> DataProcessor:
        return DataProcessor()

    @pytest.fixture
    def output_generator(self) -> OutputGenerator:
        return OutputGenerator()

    def test_parse_valid_csv(self, data_processor, csv_contents):
        record_list = data_processor.parse_csv_contents(csv_contents)
        assert (record_list is not None)
        assert (len(record_list) > 0)
        for record in record_list:
            assert isinstance(record, Record)

    def test_parse_invalid_csv(self, data_processor, csv_contents):
        position = random.randint(0, len(csv_contents))
        malformed_contents = csv_contents[:position] + \
            "," + csv_contents[position:]
        with pytest.raises(ValueError):
            data_processor.parse_csv_contents(malformed_contents)

    def test_handle_investment(self, data_processor):
        principle = 1000
        days_since_investment = 30
        rate = 0.1
        types = [InterestType.SIMPLE, InterestType.COMPOUND]
        compounding_interval = CompoundingInterval.ANNUALLY
        expected_results = [
            round(1000.0 * (1 + (.1 * 30/365)), 2),
            round(1000 * (1 + .1/1)**(1*30/365), 2)
        ]

        for type in types:
            result = data_processor.handle_investment(
                principle, rate, days_since_investment, type, compounding_interval)

            assert (result is not None)
            assert (result == expected_results.pop(0))

    def test_nonpositive_handle_investment(self, data_processor):
        principle = 100
        days_since_investment = 395
        rate = 0
        type = InterestType.SIMPLE
        compounding_interval = CompoundingInterval.ANNUALLY

        result = data_processor.handle_investment(
            principle, rate, days_since_investment, type, compounding_interval)
        assert (result is not None)
        assert (result == 100)

    def test_multiple_investments_from_file(self, data_processor, csv_contents):
        record_list = data_processor.parse_csv_contents(csv_contents)
        assert (len(record_list) > 0)
        for record in record_list:
            assert isinstance(record, Record)

    def test_multiple_time_periods(self, data_processor):
        principle = 1000
        times_since_investment = [10, 50, 100, 300, 600]
        rate = .1
        types = [InterestType.SIMPLE, InterestType.COMPOUND]
        interval = CompoundingInterval.ANNUALLY

        expected_simple_results = [
            round(1000.0 * (1 + (.1 * 10/365)), 2),
            round(1000.0 * (1 + (.1 * 50/365)), 2),
            round(1000.0 * (1 + (.1 * 100/365)), 2),
            round(1000.0 * (1 + (.1 * 300/365)), 2),
            round(1000.0 * (1 + (.1 * 600/365)), 2)
        ]

        expected_compound_results = [
            round(1000 * (1 + .1/1)**(1*10/365), 2),
            round(1000 * (1 + .1/1)**(1*50/365), 2),
            round(1000 * (1 + .1/1)**(1*100/365), 2),
            round(1000 * (1 + .1/1)**(1*300/365), 2),
            round(1000 * (1 + .1/1)**(1*600/365), 2)
        ]

        for type in types:
            if type == InterestType.SIMPLE:
                expected_results = expected_simple_results
            else:
                expected_results = expected_compound_results

            for time, expected_result in zip(times_since_investment, expected_results):
                investment_result = data_processor.handle_investment(
                    principle, rate, time, type, interval)

                assert (investment_result is not None)
                assert (investment_result == expected_result)

    def test_random_valid_csv(self, data_processor):
        random_contents = "investment id,investment name,principle,interest rate,investment date,interest type,compounding interval"
        for i in range(1000):
            random_id = hex(random.randint(0, 1048576))
            random_name = "investment " + str(i + 1)
            random_principle = random.randint(1000, 100000)
            random_rate = random.randint(0, 100)
            random_date = f"{random.randint(
                2000, 2021)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
            random_type = random.choice(["simple", "compound"])
            random_interval = random.choice(
                ["daily", "monthly", "quarterly", "annually"])
            random_contents += f"\n{random_id},{random_name},{
                random_principle},{random_rate},{random_date},{random_type},{random_interval}"

        record_list = data_processor.parse_csv_contents(random_contents)
        assert (record_list is not None)
        assert (len(record_list) == 1000)
        for record in record_list:
            assert isinstance(record, Record)


class TestOutputGenerator:

    @pytest.fixture
    def output_generator(self) -> OutputGenerator:
        return OutputGenerator()

    def test_csv_output(self, output_generator):
        records = [Record("1", "Test Investment", 1000, .1, 30,
                          InterestType.COMPOUND, CompoundingInterval.ANNUALLY, 1100)]
        csv_out = output_generator.generate_report(
            records, ReportType.PROJECTION_CSV)
        assert (csv_out is not None)
        assert (csv_out[0:5] == "inves")
        assert (csv_out.split("\n")[
                1] == "1: Test Investment | $1,000.00 invested at 10.00%, 30 days ago, compounded annually currently valued at $1,100.00")

    def test_error_output(self, output_generator):
        records = [None, None]
        csv_out = output_generator.generate_report(
            records, ReportType.PROJECTION_CSV)
        assert (csv_out[0:5] == "Error")

    def test_none_record_output(self, output_generator):
        records = [None]
        csv_out = output_generator.generate_report(
            records, ReportType.PROJECTION_CSV)
        assert (csv_out[0:5] == "Error")
        assert (csv_out.split("\n")[1] == "Invalid record detected")

    def test_negative_record_result_output(self, output_generator):
        records = [Record("1", "Test Investment", 1000, .1, 30,
                          InterestType.COMPOUND, CompoundingInterval.ANNUALLY, -100)]
        csv_out = output_generator.generate_report(
            records, ReportType.PROJECTION_CSV)
        assert (csv_out[0:5] == "Error")
        assert (csv_out.split("\n")[1] ==
                "Negative investment values detected")

    def test_empty_record_list_output(self, output_generator):
        records = []
        csv_out = output_generator.generate_report(
            records, ReportType.PROJECTION_CSV)
        assert (csv_out[0:5] == "Error")
        assert (csv_out.split("\n")[1] == "No records to process")
