import tkinter as tk

win = tk.Tk()
win.geometry("400x300")

apasari = 0
def click():
    global apasari
    apasari += 1
    # functia config din TK ne ajuta sa redefinim
    # proprietati ale elementelor de pe fereastra
    buton.config(text=f"am apasat de {apasari} ori")

buton = tk.Button(win,
                  background="lightblue",
                  text="Click me!",
                  command=click,
                  width=20, height=5)
buton.pack()


# pornim fereastra
win.mainloop()