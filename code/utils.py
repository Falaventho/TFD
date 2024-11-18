from enum import Enum


class InterestType(Enum):
    SIMPLE = 0
    COMPOUND = 1


class Record():
    # investment id,investment name,principle,interest rate,interest type,compounding interval
    def __init__(self, id: str, name: str, principle: float, interest_rate: float, time_since_investment: int, interest_type: InterestType, compounding_interval: str, result: int = None):
        self.id = id
        self.name = name
        self.interest_type = interest_type
        self.compounding_interval = compounding_interval
        self.principle = principle
        self.rate = interest_rate
        self.time_since_investment = time_since_investment
        self.type = interest_type
        self.result = result or self.__calculate_result()

    def __str__(self):
        return f"Record: {self.id}: {self.name} | {self.principle:.2f} invested at {self.rate * 100 :.2f}%, {self.time_since_investment} days ago, {self.interest_type} {self.__get_type_label()} currently valued at: {self.result}"

    def __get_type_label(self):
        match self.interest_type:
            case InterestType.SIMPLE:
                return ""
            case InterestType.COMPOUND:
                return str(self.compounding_interval)

    def __calculate_result(self):
        match self.interest_type:
            case InterestType.SIMPLE:
                return self.principle + self.principle * self.rate * self.time_since_investment
            case InterestType.COMPOUND:
                return self.principle * (1 + self.rate) ** self.time_since_investment
