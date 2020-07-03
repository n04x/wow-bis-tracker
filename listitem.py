import tkinter as tk

class ListItem:
    def __init__(self, root, row, items, headers):
        self.row = row
        scrollbar = tk.Scrollbar(root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(root, width=200, height=200, yscrollcommand=scrollbar.set)
        for item in items:
            listbox.insert(tk.END, item.printItem())
        
        listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=listbox.yview)