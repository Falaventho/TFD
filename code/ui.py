from dataprocessor import DataProcessor
from outputgenerator import OutputGenerator, ReportType
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os


class UserInterface:

    def __init__(self, root):
        self.root = root
        self.data_processor = DataProcessor()
        self.output_generator = OutputGenerator()
        self.projection_csv = None
        self._setup_ui()

    def _setup_ui(self):
        self.root.title("Investment Projection")
        self.root.geometry("500x500")

        self._setup_input_frame()

    def _setup_input_frame(self):
        self.input_frame = ttk.LabelFrame(self.root, text="Input")
        self.input_frame.pack(pady=10, fill="both", expand=True)

        self.input_label = ttk.Label(
            self.input_frame, text="Select a CSV file:")
        self.input_label.pack()

        self.input_button = ttk.Button(
            self.input_frame, text="Browse", command=self._handle_browse)
        self.input_button.pack()

        self.input_file_label = ttk.Label(self.input_frame, text="")
        self.input_file_label.pack()

        self.input_process_button = ttk.Button(
            self.input_frame, text="Process", command=self._handle_process)
        self.input_process_button.pack()

        self.input_view_button = ttk.Button(
            self.input_frame, text="View Projection CSV", command=lambda: self._display_csv(self.projection_csv))
        self.input_view_button.pack()

        self.input_write_csv_button = ttk.Button(
            self.input_frame, text="Save Output", command=self._write_output_dir)
        self.input_write_csv_button.pack()

    def _handle_browse(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")])
        self.input_file_label.config(text=file_path)

    def _handle_process(self):
        file_path = self.input_file_label.cget("text")
        if not file_path:
            messagebox.showerror("Error", "Please select a file first.")
            return

        with open(file_path, "r") as f:
            contents = f.read()

        records = self.data_processor.parse_csv_contents(contents)
        self.projection_csv = self.output_generator.generate_report(
            records, ReportType.PROJECTION_CSV)
        self.projection_html = self.output_generator.generate_report(
            records, ReportType.PROJECTION_HTML)

    def _display_csv(self, csv_contents: str):
        if not csv_contents:
            messagebox.showerror("Error", "No CSV contents to display.")
            return
        self.output_frame = ttk.LabelFrame(self.root, text="Output")
        self.output_frame.pack(pady=10, fill="both", expand=True)

        self.output_text = tk.Text(self.output_frame, width=160, height=30)
        self.output_text.pack()

        self.output_text.insert(tk.END, csv_contents)

    def _display_csv_from_vile(self, file_path: str):
        with open(file_path, "r") as f:
            contents = f.read()
        self.display_csv(contents)

    def _write_output_dir(self):
        filepath = filedialog.askdirectory(
            title="Where would you like to save the output files?")
        if filepath:
            with open(os.path.join(filepath, "projection.csv"), "w") as f:
                f.write(self.projection_csv)
            with open(os.path.join(filepath, "projection.html"), "w") as f:
                f.write(self.projection_html)
            with open(os.path.join(filepath, "styles.css"), "w") as f:
                f.write(
                    "body {background-color: rgb(12, 12, 12);color: whitesmoke;}table {border-collapse: collapse;width: 100%;text-align: left;}th {background-color: black;}tr {border-bottom: 1px solid #f2f2f2;}td {padding: 8px;}")
            messagebox.showinfo(
                "Success", "Projection files written successfully.")
        else:
            messagebox.showerror("Error", "No directory selected.")
