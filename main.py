import csv
import tkinter as tk
from item import *
from window import *
from search import *
from obtainedItem import *

root = tk.Tk()


# initialize an array of Items from CSV file.
items = []
new_items = []
with open('bis.csv') as file:
    f = csv.reader(file)
    count = 0
    for row in f:
        new_item = Item(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        items.append(new_item)
headers = ['ID', 'Slot', 'Name', 'Source', 'Location', 'Obtained', 'BiS']
headers_text = headers[0] + '\t' + headers[1] + '\t' + headers[2] + '\t' + headers[3] + '\t' + headers[4] + '\t' + headers[5] + '\t' + headers[6]
print(items[0].name)
frame = tk.Frame(root)
search_button = Search(root, len(items), items, headers)
obtain_button = ObtainedItem(root, len(items), items, headers)

root.mainloop()
