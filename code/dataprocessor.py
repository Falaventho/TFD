from utils import Record, InterestType, CompoudningInterval
from datetime import date, datetime


class DataProcessor():

    def __init__(self):
        pass

    def parse_csv_contents(self, contents: str) -> list[Record]:
        lines = contents.split("\n")
        if lines[0] != "investment id,investment name,principle,interest rate, investment date,interest type,compounding interval":
            raise ValueError("Invalid CSV format - header mismatch")

        records = []
        for line in lines:
            parts = line.split(",")
            if len(parts) != 6:
                raise ValueError(f"Invalid CSV format around {line}")

            id, name, principle, rate, investment_date, type, interval = parts

            time_since_investment = self.__calculate_days_since_investment(
                investment_date)

            record = Record(id, name, float(principle), float(
                rate), time_since_investment, InterestType[type], CompoudningInterval[interval])
            records.append(record)

        return records

    def handle_investment(self, principle: int, rate: int, time_since_investment: int, type: str) -> int:
        pass

    def __calculate_days_since_investment(self, investment_date) -> int:
        listed_date = datetime.strptime(investment_date, "%Y-%m-%d")
        return (date.today() - date(listed_date)).days
