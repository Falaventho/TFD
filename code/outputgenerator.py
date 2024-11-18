from utils import Record
from enum import Enum



class ReportType(Enum):
    PROJECTION_CSV = 0
    PROJECTION_HTML = 1
    CURRENT_CSV = 10
    CURRENT_HTML = 11


class OutputGenerator():

    def __init__(self):
        pass

    def generate_report(self, records: list[Record], type: ReportType) -> str:
        pass

    def generate_projection_csv(self, records: list[Record]) -> str:
        x = 0
        while x != len(Record):
            test = [Record(x) + ","]
            Record(x) = test
            print(Record(x))
            x+=1
        pass

    def generate_projection_html(self, records: list[Record]) -> str:
        pass

    def generate_error_output(self, errors: list[str]) -> str:
        pass
