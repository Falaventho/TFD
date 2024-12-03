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
        return f"{self.id}: {self.name} | ${self._format_money(self.principle)} invested at {self.rate * 100:.2f}%, {self.time_since_investment} days ago, {self._get_interest_type_label()} currently valued at ${self._format_money(self.result)}"

    def _get_interest_type_label(self):
        match self.interest_type:
            case InterestType.SIMPLE:
                return "accruing simple interest"
            case InterestType.COMPOUND:
                interval_label = self._get_compounding_interval_label()
                return f"compounded {interval_label}"

    def _get_interest_type_brief(self):
        match self.interest_type:
            case InterestType.SIMPLE:
                return "simple"
            case InterestType.COMPOUND:
                return "compound"

    def _get_compounding_interval_label(self):
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

    def as_csv(self):
        return f"{self.id},{self.name},{self._format_money(self.principle)},{self.rate * 100:.2f},{self.time_since_investment},{self._get_interest_type_brief()},{self._get_compounding_interval_label()},{self._format_money(self.result)}"

    def as_html_row(self):
        return f"<tr><td>{self.id}</td><td>{self.name}</td><td>{self._format_money(self.principle)}</td><td>{self.rate * 100:.2f}</td><td>{self.time_since_investment}</td><td>{self._get_interest_type_brief()}</td><td>{self._get_compounding_interval_label()}</td><td>{self._format_money(self.result)}</td></tr>"
