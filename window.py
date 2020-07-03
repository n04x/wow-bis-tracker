import tkinter as tk

class Table:
    def __init__(self, root, row, items, headers):
        self.row = row
        root.configure(bg='black')
        self.entries = []
        
        # Creating table
        ROW_DISPLACEMENT = 4
        for i in range(len(headers)):
            self.e = tk.Label(root, text=str(headers[i]), fg='white', bg='black', font=('Helvetica', 14)).grid(column=i,row=ROW_DISPLACEMENT-1)

        for i in range(row):                
            for j in range(len(items)):                
                if j == 0:
                    self.e = tk.Entry(root, width=8, font=('Arial', 12))
                    self.entries.append(self.e)
                    self.e.grid(row=i+ROW_DISPLACEMENT, column=j)
                    self.e.insert(tk.END, items[i].itemID)
                elif j == 1:
                    self.e = tk.Entry(root, width=10, font=('Arial', 12))
                    self.entries.append(self.e)
                    self.e.grid(row=i+ROW_DISPLACEMENT, column=j)
                    self.e.insert(tk.END, items[i].slot)
                elif j == 2:
                    self.e = tk.Entry(root, width=20, font=('Arial', 12))
                    self.entries.append(self.e)
                    self.e.grid(row=i+ROW_DISPLACEMENT, column=j)
                    self.e.insert(tk.END, items[i].name)
                elif j == 3:
                    self.e = tk.Entry(root, width=25, font=('Arial', 12))
                    self.entries.append(self.e)
                    self.e.grid(row=i+ROW_DISPLACEMENT, column=j)
                    self.e.insert(tk.END, items[i].source)
                elif j == 4:
                    self.e = tk.Entry(root, width=20, font=('Arial', 12))
                    self.entries.append(self.e)
                    self.e.grid(row=i+ROW_DISPLACEMENT, column=j)
                    self.e.insert(tk.END, items[i].location)  
                elif j == 5:
                    # self.e = tk.Entry(root, width=6, font=('Arial', 12))
                    # check_val = tk.BooleanVar()
                    self.e = tk.Checkbutton(root)
                    if items[i].obtained == 'TRUE':
                            self.e.select()
                    else:
                        self.e.deselect()
                    self.entries.append(self.e)
                    self.e.grid(row=i+ROW_DISPLACEMENT, column=j)
                elif j == 6:
                    self.e = tk.Entry(root, width=4, font=('Arial', 12))
                    self.entries.append(self.e)
                    self.e.grid(row=i+ROW_DISPLACEMENT, column=j)
                    self.e.insert(tk.END, items[i].bis)    

    def __del__(self):
        print('deleted')
                