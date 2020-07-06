import tkinter as tk
from search import *
from obtainedItem import *

# RESET button
def createResetButton(frame, items, headers):
    reset_button = tk.Button(frame, text='Reset')
    reset_button.grid(row=0, column=5)
    reset_button.config(command=lambda: createAllButton(frame, items, headers))

# SEARCH button
def createSearchButton(frame, items, headers):
    search_button = tk.Button(frame, text='Search')
    search_button.grid(row=0, column=1)
    search_button.config(command=lambda: searchWindow(frame, items, headers))

def searchWindow(frame, items, headers):
    search_window = Search(frame, len(items), items, headers)

# OBTAINED ITEMS button
def createObtainedButton(frame, items, headers):
    obtain_button = tk.Button(frame, text='Obtain')
    obtain_button.grid(row=0, column=2)
    obtain_button.config(command=lambda: obtainedItemWindow(frame, items, headers))

def obtainedItemWindow(frame, items, headers):
    obtain_window = ObtainedItem(frame, len(items), items, headers)

# CREATE all button
def createAllButton(frame, items, headers):
    for w in frame.winfo_children():
        w.destroy()
    createResetButton(frame, items, headers)
    createSearchButton(frame, items, headers)
    createObtainedButton(frame, items, headers)

