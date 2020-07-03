import csv
import tkinter as tk
from item import *
from window import *
from search import *
from obtainedItem import *

def main():
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
    frame = tk.Frame(root, bg = "black", width=1200, height=720)
    frame.pack(side=tk.LEFT, expand=1)
    search_button = Search(frame, len(items), items, headers)
    obtain_button = ObtainedItem(frame, len(items), items, headers)

    reset_button = tk.Button(frame, text='Reset')
    reset_button.grid(row=0, column=3)
    def resetAll():
        for w in frame.winfo_children():
            w.destroy()
        search_button = Search(frame, len(items), items, headers)
        obtain_button = ObtainedItem(frame, len(items), items, headers)
        reset_button = tk.Button(frame, text='Reset')
        reset_button.grid(row=0, column=3)

    reset_button.config(command=resetAll)

    root.mainloop()
    
if __name__ == "__main__": 
    main()