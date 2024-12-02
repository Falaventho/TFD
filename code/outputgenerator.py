from utils import Record
from enum import Enum


class ReportType(Enum):
    PROJECTION_CSV = 0
    PROJECTION_HTML = 1


class OutputGenerator():

    def __init__(self):
        pass

    def generate_report(self, records: list[Record], type: ReportType) -> str:
        """
            Args:
                records: list of records from user input.
                ReportType: The type of report to generate (e.g. if you choose to generate a report, 
                this allows you to type generate PROJECTION_CSV, instead of generate 0).
                days_since_investment: Number of days since investment.
               

            Returns:
                The user's formatted records.
        """
        if len(records) == 0:
            return self.generate_error_output(["No records to process"])

        for record in records:
            if record is None:
                return self.generate_error_output(["Invalid record detected"])
            elif record.result is None:
                return self.generate_error_output(["Records have not been processed"])
            elif record.result < 0:
                return self.generate_error_output(["Negative investment values detected"])

        match type:
            case ReportType.PROJECTION_CSV:
                return self.generate_projection_csv(records)
            case ReportType.PROJECTION_HTML:
                return self.generate_projection_html(records)

    def generate_projection_csv(self, records: list[Record]) -> str:
        """
            Args:
                records for a CSV file.

            Returns:
                String of records in CSV format.
        """
        csv = "investment id,investment name,principle,interest rate,investment date,interest type,compounding interval,projected value"
        for record in records:
            csv += "\n" + record.as_csv()

        return csv

    def generate_projection_html(self, records: list[Record]) -> str:
        """
            Args:
                records : list of document records.
                
            Returns:
                String of records in HTML format.
        """
        html = "<!DOCTYPE HTML><html><head><title>Investment Projections</title></head><body>"

        html += "<h1>Investment ID,Investment Name,Principle,Interest Rate,Investment Date,Interest Type,CompoundingInterval,Projected Value</h1>"

        for record in records:
            html += "<p>" + str(record) + "</p>"

        html += "</body></html>"

        return html

    def generate_error_output(self, errors: list[str]) -> str:
        """
            Args:
                errors: takes list of errors that have been generated.
                

            Returns:
                returns all errors that have been triggered.
        """
        e = "Error(s) detected:"
        for msg in errors:
            e += f"\n{msg}"
        return e
