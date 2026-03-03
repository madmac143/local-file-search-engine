import tkinter as tk
from tkinter import filedialog, messagebox

from scanner import scan_directory
from indexer import build_index
from search import run_search


class SearchGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Local Search Tool")
        self.root.geometry("1000x650")
        self.root.minsize(800, 500)
        self.root.resizable(True, True)

        # Create layout frames (structure) with temporary debug colors
        self.top_frame = tk.Frame(self.root, bg="red")
        self.control_frame = tk.Frame(self.root, bg="blue")
        self.results_frame = tk.Frame(self.root, bg="green")
        self.status_frame = tk.Frame(self.root, bg="yellow")

        # Place frames in the window (layout)
        self.top_frame.pack(fill="x")
        self.control_frame.pack(fill="x")
        self.results_frame.pack(fill="both", expand=True)
        self.status_frame.pack(fill="x")

        # Top Bar Widgets
        self.select_button = tk.Button(self.top_frame, text="Select Folder", command=self.choose_folder)
        self.path_label = tk.Label(self.top_frame, text="No folder selected", anchor="w")

        # Place top bar widgets
        self.select_button.pack(side="left", padx=10, pady=10)
        self.path_label.pack(side="left", fill="x", expand=True, padx=10)

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_label.config(text=folder)


if __name__ == "__main__":
    root = tk.Tk()
    app = SearchGUI(root)
    root.mainloop()
