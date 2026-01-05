import tkinter as tk

COOKIES = 0
COOKIE_GENERATORS = {
    "auto": 0,
    "truck": 0
}

def buy_auto():
    global COOKIE_GENERATORS, COOKIES
    if COOKIES >= 20:
        COOKIES -= 20
        COOKIE_GENERATORS["auto"] += 1
        buton_autoclicker.config(text=f"Buy autoclicker for 20 cookies ({COOKIE_GENERATORS["auto"]})")
        update()

def buy_truck():
    global COOKIE_GENERATORS, COOKIES
    if COOKIES >= 200:
        COOKIES -= 200
        COOKIE_GENERATORS["truck"] += 1
        buton_truck.config(text=f"Buy cookie truck for 200 cookies ({COOKIE_GENERATORS["truck"]})")
        update()

def update():
    global COOKIES
    label.config(text=f"{COOKIES} cookies")

def click():
    global COOKIES
    COOKIES += 1
    update()

def generate_cookies():
    global COOKIES, COOKIE_GENERATORS
    COOKIES += COOKIE_GENERATORS["auto"] * 1 + COOKIE_GENERATORS["truck"] * 20
    update()
    root.after(1000,generate_cookies)


root = tk.Tk()
root.geometry("400x400")
root.title("Cookie Clicker!")

root.after(1000, generate_cookies)

label = tk.Label(root, text="0 cookies")
label.pack()

button_click = tk.Button(root, text="Get cookie!", command=click)
button_click.pack()

store_label = tk.Label(root, text="STORE")
store_label.pack()

buton_autoclicker = tk.Button(text="Buy autoclicker for 20 cookies (0)", command=buy_auto)
buton_autoclicker.pack()

buton_truck = tk.Button(text="Buy cookie truck for 200 cookies (0)", command=buy_truck)
buton_truck.pack()


root.mainloop()