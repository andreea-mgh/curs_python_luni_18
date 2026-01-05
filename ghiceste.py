import tkinter as tk
from random import randint as rand

numar = rand(1, 100)
incercari = 0

def verifica():
    global incercari, numar
    incercari += 1

    # try "incearca" sa faca o actiune care e posibil sa dea erori
    # folosim "try" cand nu vrem sa se opreasca programul la erori
    # (evita crash-urile)
    try:
        n = int(entry.get())
        if n < numar:
            rezultat.config(text="prea mic!")
        elif n > numar:
            rezultat.config(text="prea mare!")
        elif n == numar:
            rezultat.config(text=f"Corect!!! Ai reusit din {incercari} incercari")
            incercari = 0
            numar = rand(1,100)
    except:
        rezultat.config(text="Scrie un numar valid!")


root = tk.Tk()
root.title("Ghiceste numarul!")
root.geometry("400x200")

label = tk.Label(root, text="Ghiceste numarul de la 1 la 100!")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Verifica", command=verifica)
button.pack(pady=10)

rezultat = tk.Label(root)
rezultat.pack(pady=10)

root.mainloop()