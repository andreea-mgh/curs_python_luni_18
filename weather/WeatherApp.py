import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import json

from PIL import Image, ImageTk

BG = "#89b4dd"
FG = "#222A28"

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicație cool care zice dacă plouă")
        self.root.geometry("890x470+300+300")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.api_key = "81b50f06ea9546e98ab143136260902"

        self.settings = {}

        self.interface()
    
    def interface(self):
        icon = tk.PhotoImage(file="Images/logo.png")
        self.root.iconphoto(False, icon)

        self.textfield = tk.Entry(self.root, width=15, justify='center',
                                  bg="#2E3B58", fg="#CEFAFC",
                                  font=('Arial', 20, 'bold'))
        self.textfield.place(x=10, y=10)
        self.textfield.focus()
        self.textfield.bind('<Return>', lambda event:self.get_weather())

        self.temp_label = tk.Label(self.root, text="??? \u00b0C",
                                   font=('Arial',60),bg=BG,fg=FG)
        self.temp_label.place(x=20,y=200)

        self.import_settings()

        self.root.mainloop()
    
    def import_settings(self):
        try:
            with open("settings.json", "r") as f:
                self.settings = json.load(f)
        except:
            self.settings = {}
        
        if "location" in self.settings:
            self.textfield.insert(0,self.settings["location"])
            self.get_weather()


    def update_data(self):
        if not self.data:
            messagebox.showerror("Eroare","Nu am date :(")
            return
        
        if self.data['current']['condition']['icon']:
            url = "https:"+self.data['current']['condition']['icon']
            response = requests.get(url)

            if response.status_code == 200:
                with open("weather_icon.png", "wb") as f:
                    f.write(response.content)
                
                pil_image = Image.open("weather_icon.png")
                # resize aici
                pil_image = pil_image.resize((250,250), Image.BILINEAR)
                tk_image = ImageTk.PhotoImage(pil_image)

                self.icon_label = tk.Label(self.root, image=tk_image, bg=BG)
                self.icon_label.image = tk_image
                self.icon_label.place(x=640,y=0)
            

        self.temp_label.config(text=f"{self.data['current']['temp_c']} \u00b0C")

    def save_data(self, location=None):
        if location:
            self.settings['location'] = self.textfield.get()
        
        with open("settings.json","w") as f:
            json.dump(self.settings,f,indent=2)
        

    def get_weather(self):
        city = self.textfield.get()
        geolocation = Nominatim(user_agent="WeatherApp")
        location = geolocation.geocode(city)

        if location is None:
            messagebox.showerror("Eroare", "Nu am găsit orașul.")
            return

        self.save_data(location=location)

        api_url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={location.latitude},{location.longitude}&aqi=no"
        response = requests.get(api_url)

        if response.status_code != 200:
            messagebox.showerror("Eroare","Eroare la preluarea datelor :(")
            return
        
        data = response.json()
        # print(data['current']['temp_c'])

        self.data = data
        self.update_data()




if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)