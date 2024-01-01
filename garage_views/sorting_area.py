import tkinter as tk
from tkinter import ttk


from model import *

class SortingArea(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master


        # Create a label to add a new object
        self.label_add_object = ttk.Label(self, text="Object Name")
        self.label_add_object.grid(column=0, row=0)
        self.entry_add_object = ttk.Entry(self, width=50)
        self.entry_add_object.grid(column=1, row=0)
        self.button_add_object = ttk.Button(self, text="Create Object", command=lambda: self.AddObject(self.entry_add_object.get()))
        self.button_add_object.grid(column=2, row=0)

        # Create a list box in the object distribution frame
        self.listbox_object_distribution = tk.Listbox(self, width=50, height=20)
        self.listbox_object_distribution.grid(column=0, row=1,columnspan=3, sticky="nsew")

        # Add callback when the listbox line is selected
        self.listbox_object_distribution.bind('<<ListboxSelect>>', self.OnSelectObject)

        self.RefreshObjectsInVault()

        self.master.updated_db.trace("w", self.RefreshObjectsInVault)

    def RefreshObjectsInVault(self, *args):
        """
        Refresh the list of objects in the vault
        """
        self.objects_in_vault = GetObjectsInVault()
        print(self.objects_in_vault)
        # Clear all the objects in the listbox
        self.listbox_object_distribution.delete(0, tk.END)

        for object in self.objects_in_vault:
            self.listbox_object_distribution.insert(tk.END, object[1])

    def AddObject(self, object_name):
        """ 
        Add an object to the vault
        """
        print(object_name)
        AddObjectToVault(object_name)

        # Empty the text in the entry
        self.entry_add_object.delete(0, tk.END)

        self.master.updated_db.set(1)

    def OnSelectObject(self, event):
        """
        Callback when an object is selected in the listbox
        """
        # Get the selected line index
        widget = event.widget
        selection=widget.curselection()
        print("Selection:", selection)
        # Check if selection is ()
        if len(selection) == 0:
            print("No selection")  
        else:
            index = selection[0]
            object_name = widget.get(index)
            print("Selected object:", object_name)
            object_id = self.objects_in_vault[index][0]
            print("Selected object id:", object_id)
            self.master.last_selected_object_sorting.set(object_id)
            self.master.last_selected_object_general.set("sorting")
