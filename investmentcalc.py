

class UserInterface():

    pass


class DataProcessor():

    def __init__(self):
        pass

    def parse_csv_contents(self, contents: str) -> list[str]:
        return []

    def handle_investment(self, principle: int, rate: int, time_since_investment: int, type: str) -> int:
        pass


class OutputGenerator():

    def __init__(self):
        pass

    def generate_projection_csv(self, records: list) -> str:
        pass


class Record():

    def __init__(self):
        pass
