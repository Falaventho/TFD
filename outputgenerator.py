from utils import Record
from enum import Enum


class ReportType:
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
        pass

    def generate_projection_html(self, records: list[Record]) -> str:
        pass

    def generate_error_output(self, errors: list[str]) -> str:
        pass
