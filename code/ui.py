from dataprocessor import DataProcessor
from outputgenerator import OutputGenerator
from utils import Record
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class UserInterface:

    def __init__(self, root):
        self.root = root
        self.data_processor = DataProcessor()
        self.output_generator = OutputGenerator()
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
        projection_csv = self.output_generator.generate_projection_csv(records)

        with open("projection.csv", "w") as f:
            f.write(projection_csv)

        messagebox.showinfo("Success", "Projection saved to projection.csv")
