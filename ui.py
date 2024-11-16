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
