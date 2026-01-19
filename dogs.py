import requests
from random import randint as rand

breed = input("Dog breed: ")

if breed == "":
    response = requests.get("https://dog.ceo/api/breeds/image/random")
else:
    response = requests.get("https://dog.ceo/api/breed/"+breed+"/images")
data = response.json()

if data["status"] != "success":
    print("error :(")
else:
    if breed == "":
        print(data["message"])
    else:
        length = len(data["message"])
        number = rand(0,length)
        print(number, data["message"][number])