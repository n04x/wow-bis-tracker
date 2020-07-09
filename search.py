import tkinter as tk
from window import *
from headerbutton import *

class Search:
    def __init__(self, root, row, items, headers):
        # Create Search(s)
        # Search by Slot
        self.slot_label = tk.Label(root, text='Item Slot to search', font=('Helvetica 12 bold')).grid(row=2, columnspan=3, sticky=tk.W)
        
        self.slot_entry = tk.Entry(root)
        self.slot_entry.grid(row=2, column=3)

        self.find_slot = tk.Button(root, text='Find')
        self.find_slot.grid(row=2, column=4)
        
        # Search by Location
        self.location_label = tk.Label(root, text='Item Location to search: ', font=('Helvetica 12 bold')).grid(row=1, columnspan=3, sticky=tk.W)
        
        self.location_entry = tk.Entry(root)
        self.location_entry.grid(row=1, column=3)
        
        self.find_location = tk.Button(root, text='Find')
        self.find_location.grid(row=1, column=4)

        # Search result data.
        self.results = []
        self.count = 0
        self.table = None
        # self.reset = False
        
        # Search(s) functions
        def findLocation():
            # self.results.clear()
            search_location = self.location_entry.get()
            
            if search_location:
                for item in items:
                    if search_location == item.location:
                        self.results.append(item)
            self.table = Table(root, len(self.results), self.results, headers)

        def findSlot():
            search_slot = self.slot_entry.get()

            if search_slot:
                for item in items:
                    if search_slot == item.slot:
                        self.results.append(item)
            self.table = Table(root, len(self.results), self.results, headers)

        self.find_slot.config(command=findSlot)
        self.find_location.config(command=findLocation)
        
