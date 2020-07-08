import tkinter as tk

l = [[0,0,0,0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
n = len(l)      #this is the length of the list l
lngt = 400 // n #this is the dimension of the squares that I want

fen = tk.Tk()
fen.geometry("600x400")

#I would like to create a table of 4 rows on canvas
#each row should contain 4 squares
can = tk.Canvas(fen, width=450, height=400, bg="lightblue")
can.pack(side=tk.LEFT)

for i in range(n):
    y = i * lngt
    for j in range(n):
        x = j * lngt
        can.create_rectangle(x, y, x+lngt, y+lngt, fill="red")

f = tk.Frame(fen, width=150, height=400, bg="lightcoral")
f.pack(side=tk.LEFT)

fen.mainloop()