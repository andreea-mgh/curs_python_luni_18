
from random import shuffle
import tkinter as tk

text = "IMI PLACE SA MA JOC MINECRAFT PE HYPIXEL PENTRU CA AU EVENIMENTE COOL DE SARBATORI"
# text = "AM PRIMIT O JUCARIE VALOROASA LABUBU DE AUR 24K SI AM PUS-O IN DULAP"

ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHEIE = {}

def generate_key(cipher):
    global CHEIE

    if cipher == "Caesar":
        # CAESAR CIPHER
        for i in range(len(ALFABET)):
            CHEIE[ALFABET[i]] = ALFABET[(i+2) % len(ALFABET)]

    elif cipher == "Atbash":
        # ATBASH CIPHER
        for i in range(len(ALFABET)):
            CHEIE[ALFABET[i]] = ALFABET[-i-1]

    elif cipher == "Substitution":
        # RANDOM SUBSTITUTION CIPHER
        shuffled = list(ALFABET[:]) 
        shuffle(shuffled)
        for i in range(len(ALFABET)):
            CHEIE[ALFABET[i]] = shuffled[i]

generate_key("Atbash")

# CRIPTARE
def encrypt():
    text = input_text.get("1.0", tk.END).upper()
    rezultat = ''
    for litera in text:
        if litera in CHEIE:
            rezultat += CHEIE[litera]
        else:
            rezultat += litera
    rezultat_label.config(text=rezultat)

def decrypt():
    text = input_text.get("1.0", tk.END).upper()
    rezultat = ''
    # inverseaza cheile si valorile din dictionar
    CHEIE_INVERS = {v:k for k,v in CHEIE.items()} 
    for litera in text:
        if litera in CHEIE_INVERS:
            rezultat += CHEIE_INVERS[litera]
        else:
            rezultat += litera
    rezultat_label.config(text=rezultat)

win = tk.Tk()

input_text = tk.Text(win, width=50, height=10)
input_text.pack()

buton = tk.Button(win, text="Encrypt!", command=encrypt)
buton.pack()

rezultat_label = tk.Label(win, text='')
rezultat_label.pack()

win.mainloop()

# print(rezultat)
