from investment_calc import *


class TestFrontend:

    @pytest.fixture
    def csv_contents(self) -> str:
        with open("example.csv", "r") as f:
            contents = f.read()
        return contents

    @pytest.fixture
    def data_processor(self):
        return DataProcessor()

    def test_parse_valid_csv(self):

        contents_list = data_processor.parse_csv_contents(csv_contents)
        for record in contents_list:
            assert (len(record) == 6)
