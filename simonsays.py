import tkinter as tk

CULORI = [
    "#22E861",
    "#E8E822",
    "#B81717",
    "#0694BB"
]

CULORI_LIGHT = [
    "#8FFFB3",
    "#FFFFA9",
    "#FFA2A2",
    "#9CE8FD"
]

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

        # Canvas
        self.canvas = tk.Canvas(
            self.root,
            width = 400,
            height= 400,
            bg=self.BG_COLOR,
            highlightthickness=0
        )
        self.canvas.pack()

        # Butoanele
        coords = [
            (0, 50, 50),
            (1, 250, 50),
            (2, 50, 250),
            (3, 250, 250)
        ]
        self.butoane = []
        for culoare, x, y in coords:
            buton = self.canvas.create_rectangle(
                x, y, x+100, y+100,
                fill=CULORI[culoare],
                outline = "black",
                width = 15,
            )

            self.butoane.append(buton)

            self.canvas.tag_bind(
                buton,
                "<Button-1>",
                lambda event, c=culoare: self.blink(c),
            )

        
        # Buton start
        self.start_button = tk.Button(
            self.root,
            text = "START",
            bg="#240F36",
            fg=self.TEXT_COLOR,
            font=('Arial',18)
        )
        self.start_button.pack()

    def blink(self, col):
        self.canvas.itemconfig(
            self.butoane[col],
            fill=CULORI_LIGHT[col],
            outline=CULORI[col]
        )
        self.root.after(100, lambda:self.reset_light(col))
    
    def reset_light(self, col):
        self.canvas.itemconfig(
            self.butoane[col],
            fill=CULORI[col],
            outline="black"
        )



win = tk.Tk()
app = Interfata(win)
win.mainloop()
