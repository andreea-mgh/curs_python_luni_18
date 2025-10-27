import tkinter as tk

def chestie():
    print("ai apasat butonul")

# facem un obiect fereastra, il numim "win"
win = tk.Tk()
# facem un obiect buton, il numim "button"
# il cream cu atributele:
#    textul de pe buton "click me"
#    comanda "chestie"
button = tk.Button(win, text="click me", command=chestie)
# afiseaza butonul pe fereastra
button.pack()

win.mainloop()


# Toate functiile au paranteze dupa nume.

# Cand cream un obiect, si acolo punem paranteze
# dupa numele obiectului

# Rolul parantezelor e sa transmitem informatii catre
# chestia dupa care punem paranteze.
#    ex. la functii transmitem parametri
#        la obiecte transmitem trasaturile obiectelor

# functiile sunt cu litere mici
# obiectele cu litere mari