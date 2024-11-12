from investmentcalc import *
import pytest


class TestFrontend:

    @pytest.fixture
    def csv_contents(self) -> str:
        with open("example.csv", "r") as f:
            contents = f.read()
        return contents

    @pytest.fixture
    def data_processor(self) -> DataProcessor:
        return DataProcessor()

    def test_parse_valid_csv(self, data_processor, csv_contents):
        record_list = data_processor.parse_csv_contents(csv_contents)
        for record in record_list:
            assert isinstance(record, Record)

    def test_parse_invalid_csv(self, data_processor):
        with pytest.raises(ValueError):
            data_processor.parse_csv_contents("")

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
                assert data_processor.handle_investment(
                    principle, rate, time_since_investment, type) == expected_results.pop(0)

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
                assert data_processor.handle_investment(
                    principle, rate, time_since_investment, type) == expected_results.pop(0)

    def test_multiple_investments_from_file(self, data_processor, csv_contents):
        record_list = data_processor.parse_csv_contents(csv_contents)
        for record in record_list:
            assert data_processor.handle_investment(
                record.principle, record.rate, record.time_since_investment, record.type) == record.result
