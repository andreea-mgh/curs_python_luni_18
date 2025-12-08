
from random import shuffle
import tkinter as tk

text = "IMI PLACE SA MA JOC MINECRAFT PE HYPIXEL PENTRU CA AU EVENIMENTE COOL DE SARBATORI"
# text = "AM PRIMIT O JUCARIE VALOROASA LABUBU DE AUR 24K SI AM PUS-O IN DULAP"

ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHEIE = {}

# CAESAR CIPHER
# for i in range(len(ALFABET)):
#     CHEIE[ALFABET[i]] = ALFABET[(i+2) % len(ALFABET)]

# ATBASH CIPHER
for i in range(len(ALFABET)):
    CHEIE[ALFABET[i]] = ALFABET[-i-1]

# RANDOM SUBSTITUTION CIPHER
shuffled = list(ALFABET[:]) 
shuffle(shuffled)
for i in range(len(ALFABET)):
    CHEIE[ALFABET[i]] = shuffled[i]

# CRIPTARE
def encrypt():
    rezultat = ''
    for litera in text:
        if litera in CHEIE:
            rezultat += CHEIE[litera]
        else:
            rezultat += litera
    rezultat_label.config(text=rezultat)

win = tk.Tk()

buton = tk.Button(win, text="Encrypt!", command=encrypt)
buton.pack()

rezultat_label = tk.Label(win, text='')
rezultat_label.pack()

win.mainloop()

# print(rezultat)
