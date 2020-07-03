import tkinter as tk
from window import *

class Search:
    def __init__(self, root, row, items, headers):
        # Create Search
        self.search1 = tk.Label(root, text='Item Location to search: ', bg='black', fg='white', font=('Helvetica 18 bold')).grid(row=0, column=0)
        self.e1 = tk.Entry(root)
        self.e1.grid(row=0, column=1)
        self.search_button = tk.Button(root, text='Search')
        self.search_button.grid(row=0, column=2)

        self.results = []
        self.count = 0
        self.table = None
        self.reset = False
    
        def searchItem():
            # self.results.clear()
            search_location = self.e1.get()
            
            if search_location:
                for item in items:
                    if search_location == item.location:
                        self.results.append(item)
            self.table = Table(root, len(self.results), self.results, headers)
            print('button clicked')

        self.search_button.config(command=searchItem)
        
