from enum import Enum


class InterestType(Enum):
    SIMPLE = "simple"
    COMPOUND = "compound"


class CompoundingInterval(Enum):
    DAILY = "daily"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    ANNUALLY = "annually"


class Record():
    # investment id,investment name,principle,interest rate,interest type,compounding interval
    def __init__(self, id: str, name: str, principle: float, interest_rate: float, time_since_investment: int, interest_type: InterestType, compounding_interval: str, result: float = None):
        self.id = id
        self.name = name
        self.interest_type = interest_type
        self.compounding_interval = compounding_interval
        self.principle = principle
        self.rate = interest_rate
        self.time_since_investment = time_since_investment
        self.type = interest_type
        self.result = result

    def __str__(self):
        return f"{self.id}: {self.name} | ${self._format_money(self.principle)} invested at {self.rate * 100:.2f}%, {self.time_since_investment} days ago, {self.__get_interest_type_label()} currently valued at ${self._format_money(self.result)}"

    def __get_interest_type_label(self):
        match self.interest_type:
            case InterestType.SIMPLE:
                return "accruing simple interest"
            case InterestType.COMPOUND:
                interval_label = self.__get_compounding_interval_label()
                return f"compounded {interval_label}"

    def __get_compounding_interval_label(self):
        match self.compounding_interval:
            case CompoundingInterval.DAILY:
                return "daily"
            case CompoundingInterval.MONTHLY:
                return "monthly"
            case CompoundingInterval.QUARTERLY:
                return "quarterly"
            case CompoundingInterval.ANNUALLY:
                return "annually"

    def _format_money(self, amount: float):
        return f'{amount:,.2f}'
