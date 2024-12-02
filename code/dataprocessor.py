from utils import Record, InterestType, CompoundingInterval
from datetime import date, datetime


class DataProcessor():

    def __init__(self):
        pass

    def parse_csv_contents(self, contents: str) -> list[Record]:
        lines = contents.split("\n")
        if lines[0] != "investment id,investment name,principle,interest rate,investment date,interest type,compounding interval":
            raise ValueError("Invalid CSV format - header mismatch")

        records = []
        for line in lines[1:]:
            parts = line.split(",")
            if len(parts) != 7:
                raise ValueError(f"Invalid CSV format around {line}")

            id, name, principle, rate, investment_date, type, interval = parts

            time_since_investment = self._calculate_days_since_investment(
                investment_date)

            record = Record(
                id,
                name,
                float(principle),
                float(rate) * .01,
                time_since_investment,
                InterestType[type.upper()],
                CompoundingInterval[interval.upper()],
            )

            record.result = self.handle_investment(
                record.principle, record.rate, record.time_since_investment, record.type, record.compounding_interval)

            records.append(record)

        return records

    def _calculate_days_since_investment(self, investment_date: str) -> int:
        listed_date = datetime.strptime(investment_date, "%Y-%m-%d")
        return (date.today() - listed_date.date()).days

    def handle_investment(self, principal: float, interest_rate: float, days_since_investment: str, interest_type: InterestType, compounding_interval: CompoundingInterval) -> float:
        """
            Args:
                principal: Initial amount invested.
                interest_rate: Annual interest rate for investment (e.g., 0.05 for 5%)
                investment_date: Date of investment in the format "YYYY-MM-DD"
                interest_type: Type of interest calculation (simple or compound)
                compounding_interval: How often the interest is compounded (daily, monthly, quarterly, annually)

            Returns:
                Tuple of calculated interest and total amount after interest.
        """

        if interest_type == InterestType.SIMPLE:
            interest = self._calculate_simple_interest(
                principal, interest_rate, days_since_investment)
        elif interest_type == InterestType.COMPOUND:
            interest = self._calculate_compound_interest(
                principal, interest_rate, days_since_investment, compounding_interval)
        else:
            raise ValueError("Invalid interest type")

        total_amount = principal + interest

        return round(total_amount, 2)

    # Calculates simple interest
    def _calculate_simple_interest(self, principal: float, interest_rate: float, days_since_investment: int) -> float:
        """
            Args:
                principal: Initial amount invested.
                interest_rate: Annual interest rate for investment (e.g., 0.05 for 5%)
                days_since_investment: Number of days since investment

            Returns:
                Calculated simple interest.
        """

        # simple interest calculation
        years = days_since_investment / 365
        interest = (principal * interest_rate * years)
        # simplify to two decimal places
        interest = round(interest, 2)

        return interest

    def _calculate_compound_interest(self, principal: float, interest_rate: float, days_since_investment: int, compounding_interval: CompoundingInterval) -> float:
        """
            Args:
                principal: Initial amount invested.
                interest_rate: Annual interest rate as a decimal (e.g., 0.05 for 5%)
                days_since_investment: Number of days since investment
                compounding_interval: How often the interest is compounded (daily, monthly, quarterly, annually)

            Returns:
                Calculated compound interest.
        """

        match compounding_interval:
            case CompoundingInterval.DAILY:
                n = 365
            case CompoundingInterval.MONTHLY:
                n = 12
            case CompoundingInterval.QUARTERLY:
                n = 4
            case CompoundingInterval.ANNUALLY:
                n = 1
            case _:
                raise ValueError("Invalid compounding interval")

        # Calculate compound interest over the course of t years
        # a = final amount
        t = days_since_investment / 365
        a = principal * (1 + interest_rate/n)**(n*t)
        interest = a - principal
        # Simplify to two decimal places
        interest = round(interest, 2)

        return interest
