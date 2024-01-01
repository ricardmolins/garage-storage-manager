import tkinter as tk
from tkinter import ttk

from model import *

class ObjectDistribution(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.columnconfigure(0, weight=1) 
        self.rowconfigure(0, weight=1)

        # Create a Treeview widget
        self.tree = ttk.Treeview(self)
        self.tree.grid(row=0, column=0,sticky="nsew")

        self.RefreshTree()

        # Add callback when the tree line is selected
        self.tree.bind('<<TreeviewSelect>>', self.OnSelectObject)

        self.master.updated_db.trace("w", self.RefreshTree)

    def RefreshTree(self, *args):
        # Clear the tree
        self.tree.delete(*self.tree.get_children())

        # Get objects in home 
        objects_in_home = GetObjectsInId(HOME_OBJECT_ID)

        # Add objects to tree at top level
        for object in objects_in_home:
            self.tree.insert("", "end", object[DB_OBJECT_ID_INDEX], text=object[DB_OBJECT_NAME_INDEX])
            # Add children
            self.AddChildren(object[DB_OBJECT_ID_INDEX])

    def OnSelectObject(self, event):
        """
        Callback when an object is selected in the tree
        """
        # Get the selected line index
        widget = event.widget
        selected_line = widget.focus()
        # Get the object_id of the selected line
        self.master.last_selected_object_distribution.set(selected_line)
        # Get the object name of the selected line
        self.master.last_selected_object_general.set(widget.item(selected_line)["text"])

        print("Selected object: ", selected_line)
        print("Selected object name: ", widget.item(selected_line)["text"])

        self.master.last_selected_object_general.set("distribution")

    def AddChildren(self, parent_id):
        # Get objects in parent_id
        objects_in_parent = GetObjectsInId(parent_id)

        # Add objects to tree at top level
        for object in objects_in_parent:
            self.tree.insert(parent_id, "end", object[DB_OBJECT_ID_INDEX], text=object[DB_OBJECT_NAME_INDEX])
            # Add children
            self.AddChildren(object[DB_OBJECT_ID_INDEX])








  