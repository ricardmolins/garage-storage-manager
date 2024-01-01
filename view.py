import tkinter as tk
from tkinter import ttk

from model import *

from garage_views.side_buttons import *
from garage_views.object_distribution import *
from garage_views.sorting_area import * 

class SortGarageGui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Create variables to store the last selected object
        self.last_selected_object_sorting = tk.IntVar(value=0)
        self.last_selected_object_distribution = tk.IntVar(value=0)
        self.last_selected_object_general = tk.StringVar(value="None")
        self.updated_db = tk.IntVar(value=0)

        # Assign weights to the rows and columns
        self.rowconfigure(0, weight=80)
        self.rowconfigure(1, weight=20)
        self.columnconfigure(0, weight=70)
        self.columnconfigure(1, weight=30)
        
        # Create 3 subframes
        self.frame_object_distribution = ObjectDistribution(self)
        self.frame_sorting_area = SortingArea(self)
        self.frame_side_buttons = SideButtons(self)

        self.frame_object_distribution.grid(column=0, row=0, sticky="nsew")
        self.frame_sorting_area.grid(row=1, column=0, pady=10, sticky="nsew")
        self.frame_side_buttons.grid(row=0,column=1, rowspan=2, padx=10, sticky="nsew")

 
        






