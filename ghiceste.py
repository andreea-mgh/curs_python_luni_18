import tkinter as tk
from random import randint as rand

numar = rand(1, 100)
incercari = 0

root = tk.Tk()
root.title("Ghiceste numarul!")
root.geometry("400x200")

label = tk.Label(root, text="Ghiceste numarul de la 1 la 100!")
label.pack()

entry = tk.Entry(root)
entry.pack()

root.mainloop()