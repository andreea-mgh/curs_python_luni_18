import tkinter as tk

class Interfata:
    def __init__(self, root):
        self.BG_COLOR = "#3B284B"
        self.TEXT_COLOR = "#AED6D8"

        self.root = root
        self.root.title("Joc cool cu beculete Simon Spune")
        self.root.geometry("500x600")
        self.root.config(background=self.BG_COLOR)

        # Scor
        self.scor_label = tk.Label(
            self.root,
            text="SCOR: 0",
            background=self.BG_COLOR,
            foreground=self.TEXT_COLOR,
            font=("Arial", 18)
        )
        self.scor_label.pack()


win = tk.Tk()
app = Interfata(win)
win.mainloop()