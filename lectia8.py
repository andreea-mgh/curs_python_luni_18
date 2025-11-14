import tkinter as tk


win = tk.Tk()
win.minsize(300,300)
win.title("Aplicatie cool in Python")

def change_theme():
    selection = theme.get()
    win.config(background=selection)
    for i in interface:
        i.config(background=selection)
    
    option = log.get()
    if option:
        print(f"changed theme to {selection}")



theme = tk.StringVar(value='white')
log = tk.BooleanVar(value=False)


interface = []
# scriu valoarea "value" in variabila "variable" cand sunt apasate
interface.append(tk.Radiobutton(win, text="Alb", value='white', variable=theme))
interface.append(tk.Radiobutton(win, text="Albastru", value='cadetblue1', variable=theme))
interface.append(tk.Radiobutton(win, text="Verde", value='darkolivegreen1', variable=theme))

interface.append(tk.Button(win, text="Schimba culoarea", command=change_theme))

# scrie True sau False in variabila "variable"
interface.append(tk.Checkbutton(win, text="scrie in terminal", variable=log))

for i in interface:
    i.pack(anchor='w')



win.mainloop()