import tkinter as tk
from tkinter import ttk

from model import *
from garage_views.object_distribution import *
from garage_views.sorting_area import *

SIDE_BUTTONS_Y_PAD = 5

class SideButtons(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Add 4 buttons to the side frame
        self.button_add_object = ttk.Button(self, text="Add Object")
        self.button_add_object.grid(row=0, column=0, sticky="nsew", pady=SIDE_BUTTONS_Y_PAD)
        self.button_edit_object = ttk.Button(self, text="Edit Object")
        self.button_edit_object.grid(row=1, column=0, sticky="nsew", pady=SIDE_BUTTONS_Y_PAD)
        self.button_delete_object = ttk.Button(self, text="Delete Object")
        self.button_delete_object.grid(row=2, column=0 ,sticky="nsew", pady=SIDE_BUTTONS_Y_PAD)
        self.button_move_object = ttk.Button(self, text="Move Object")
        self.button_move_object.grid(row=3, column=0 ,sticky="nsew", pady=SIDE_BUTTONS_Y_PAD)

        # Add callback when the buttons are clicked
        self.button_add_object.bind("<Button-1>", self.OnAddObject)
        self.button_edit_object.bind("<Button-1>", self.OnEditObject)
        self.button_delete_object.bind("<Button-1>", self.OnDeleteObject)
        self.button_move_object.bind("<Button-1>", self.OnMoveObject)


        self.edit_var_name = tk.StringVar(value="None")
        self.edit_var_id = tk.IntVar(value=0)

    def OnAddObject(self, event):
        """
        Callback when the Add Object button is clicked
        """
        print("Add Object")

        # Get last selected objects
        last_selected_object_sorting = self.master.last_selected_object_sorting.get()
        last_selected_object_distribution = self.master.last_selected_object_distribution.get()

        # Check if both are ids are not 0
        if last_selected_object_sorting != 0 and last_selected_object_distribution != 0:
            SetObjectParent(last_selected_object_sorting, last_selected_object_distribution)
            self.master.updated_db.set(1)
    def OnEditObject(self, event):
        """
        Callback when the Edit Object button is clicked
        """
        print("Edit Object")

        # Get the last selected object
        last_selected_object = self.master.last_selected_object_general.get()
        print("Last selected object: ", last_selected_object)
        if last_selected_object == "sorting":
            # Get the last selected object
            last_selected_sorting = self.master.last_selected_object_sorting.get()
            print("Value of current_name_var: ", self.edit_var_name.get())
            self.CreatePopupWindow(last_selected_sorting)
        elif last_selected_object == "distribution":
            last_selected_distribution = self.master.last_selected_object_distribution.get()
            print("Value of current_name_var: ", self.edit_var_name.get())
            self.CreatePopupWindow(last_selected_distribution)

    def CreatePopupWindow(self, object_id):
        self.edit_var_id.set(object_id)

        # Create a pop up window to edit the object
        self.master.popup_window = tk.Toplevel()
        self.master.popup_window.wm_title("Edit Object")
        self.master.popup_window.geometry("300x100")
        self.master.popup_window.resizable(False, False)
        self.master.popup_window.grid()

        # Create a label to add a new object
        current_name = GetNameOfObject(object_id)
        self.label_edit_object = ttk.Label(self.master.popup_window, text="Object Name")
        self.label_edit_object.grid(column=0, row=0)
        self.entry_edit_object = tk.Entry(self.master.popup_window,textvariable=self.edit_var_name)
        self.entry_edit_object.grid(column=1, row=0)
        self.edit_var_name.set(current_name)

        # Create a button to save the change
        self.button_save_object = ttk.Button(self.master.popup_window, text="Save")
        self.button_save_object.grid(column=0, row=1, rowspan=2)
        self.button_save_object.bind("<Button-1>", self.OnSaveChangeOnObject)

    
    def OnSaveChangeOnObject(self, event):
        """
        Callback when the Save button is clicked
        """
        print("Save Change")

        EditObject(self.edit_var_id.get(), self.edit_var_name.get())
        self.master.frame_sorting_area.RefreshObjectsInVault()
        self.master.frame_object_distribution.RefreshTree()
        self.master.popup_window.destroy()

        self.master.updated_db.set(1)
        
    
    def OnDeleteObject(self, event):
        """
        Callback when the Delete Object button is clicked
        """
        print("Delete Object")

        # Get the last selected object
        last_selected_object = self.master.last_selected_object_general.get()

        if last_selected_object == "sorting":
            # Get the last selected object
            last_selected_object = self.master.last_selected_object_sorting.get()
            DeleteObject(last_selected_object)
            self.master.updated_db.set(1)
        elif last_selected_object == "distribution":
            # Get the last selected object
            last_selected_object = self.master.last_selected_object_distribution.get()
            DeleteObject(last_selected_object)
            self.master.updated_db.set(1)
        else:
            print("No object selected")
    
    def OnMoveObject(self, event):
        """
        Callback when the Move Object button is clicked
        """
        print("Move Object")

        self.master.updated_db.set(1)
