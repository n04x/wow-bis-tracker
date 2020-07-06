import tkinter as tk
import csv

class ObtainedItem:
    def __init__(self, root, row, items, headers):
        self.ROW_DISPLACEMENT = 1
        self.obtain_label = tk.Label(root, text='Obtained item:', bg='black', fg='white', font=('Helvetica 18 bold')).grid(row=self.ROW_DISPLACEMENT, columnspan=3, sticky=tk.W)
        self.obtain_entry = tk.Entry(root)
        self.obtain_entry.grid(row=self.ROW_DISPLACEMENT, column=3)
        self.obtain_button = tk.Button(root, text='Submit')
        self.obtain_button.grid(row=self.ROW_DISPLACEMENT, column=4)

        def SetObtained():
            self.obtain_txt = self.obtain_entry.get()
            for item in items:
                if self.obtain_txt == item.name:
                    item.obtained = 'TRUE'            
            file = csv.writer(open('bis.csv', 'w'), delimiter=',')
            for item in items: 
                file.writerow([item.itemID] + [item.slot] + [item.name] + [item.source] + [item.location] + [item.obtained] + [item.bis])
                

        self.obtain_button.config(command=SetObtained)

        
