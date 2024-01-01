
from model import *
import tkinter as tk
from view import *

if __name__ == "__main__":
  
    # Create the main application window
    root = tk.Tk()
    root.title("Storage Manager")
    root.resizable(True, True)
    root.geometry("1000x900")
    # Configure row and column weights
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create an instance of the SampleFrame class and attach it to the main window
    app = SortGarageGui(master=root)

    # Run the Tkinter event loop
    app.grid(sticky="nsew")
    app.mainloop()