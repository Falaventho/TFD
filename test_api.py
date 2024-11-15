from investmentcalc import *
import pytest
import random


class TestDataProcessor:

    @pytest.fixture
    def csv_contents(self) -> str:
        with open("example.csv", "r") as f:
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
        position = random.range(0, len(csv_contents))
        malformed_contents = csv_contents[:position] + \
            "," + csv_contents[position:]
        with pytest.raises(ValueError):
            data_processor.parse_csv_contents(malformed_contents)

    def test_handle_investment(self, data_processor):
        principle = 1000
        time_since_investment = 5
        rates = [10, 20, 30]
        types = ["simple", "compound"]
        expected_results = [
            1000 + 1000 * 10 / 100 * time_since_investment,
            1000 * (1 + 10 / 100) ** time_since_investment,
            1000 + 1000 * 20 / 100 * time_since_investment,
            1000 * (1 + 20 / 100) ** time_since_investment,
            1000 + 1000 * 30 / 100 * time_since_investment,
            1000 * (1 + 30 / 100) ** time_since_investment
        ]

        for rate in rates:
            for type in types:
                result = data_processor.handle_investment(
                    principle, rate, time_since_investment, type)

                assert (result is not None)
                assert (result == expected_results.pop(0))

    def test_nonpositive_handle_investment(self, data_processor):
        principle = 1000
        time_since_investment = 5
        rates = [0, -10]
        types = ["simple", "compound"]
        expected_results = [
            1000,
            1000,
            1000 + 1000 * -10 / 100 * time_since_investment,
            1000 * (1 + -10 / 100) ** time_since_investment
        ]

        for rate in rates:
            for type in types:
                result = data_processor.handle_investment(
                    principle, rate, time_since_investment, type)

                assert (result is not None)
                assert (result == expected_results.pop(0))

    def test_multiple_investments_from_file(self, data_processor, csv_contents):
        record_list = data_processor.parse_csv_contents(csv_contents)
        assert (len(record_list) > 0)
        for record in record_list:
            assert isinstance(record, Record)

    def test_multiple_time_periods(self, data_processor):
        principle = 1000
        times_since_investment = [1, 2, 3, 4, 5]
        rate = 10
        types = ["simple", "compound"]
        expected_results = [
            1000 + 1000 * 10 * 1,
            1000 + 1000 * 10 * 2,
            1000 + 1000 * 10 * 3,
            1000 + 1000 * 10 * 4,
            1000 + 1000 * 10 * 5,
            1000 * (1 + 10 / 100) ** 1,
            1000 * (1 + 10 / 100) ** 2,
            1000 * (1 + 10 / 100) ** 3,
            1000 * (1 + 10 / 100) ** 4,
            1000 * (1 + 10 / 100) ** 5
        ]

        for type in types:
            for time in times_since_investment:
                investment_result = data_processor.handle_investment(
                    principle, rate, time, type)

                assert (investment_result is not None)
                assert (investment_result == expected_results.pop(0))

    def test_random_valid_csv(self, data_processor):
        random_contents = "investment id,investment name,principle,interest rate,interest type,compounding interval"
        for i in range(1000):
            random_id = hex(random.randint(0, 1048576))
            random_name = "investment " + str(i + 1)
            random_principle = random.randint(1000, 100000)
            random_rate = random.randint(0, 100)
            random_type = random.choice(["simple", "compound"])
            random_interval = random.randint(1, 10)
            random_contents += f"\n{random_id},{random_name},{random_principle},{random_rate},{random_type},{random_interval}"

        record_list = data_processor.parse_csv_contents(random_contents)
        assert (record_list is not None)
        assert (len(record_list) == 1000)
        for record in record_list:
            assert isinstance(record, Record)


class TestOutputGenerator:

    @ pytest.fixture
    def output_generator(self) -> OutputGenerator:
        return OutputGenerator()

    def test_csv_output(self, output_generator):
        records = [Record(1000, 10, 5, "simple", 1000 + 1000 * 10 * 5)]
        csv_out = output_generator.generate_projection_csv(records)
        assert (
            csv_out == "principle,rate,time_since_investment,type,result\n1000,10,5,simple,1500\n")

    def test_error_output(self, output_generator):
        records = [1000]
        csv_out = output_generator.generate_projection_csv(records)
        assert (csv_out[0:5] == "Error")
