import requests

URL = "http://192.168.1.135:5000"

response = requests.get(URL+'/salut')
print(response.json())

response = requests.post(URL+'/prieten', json={"nume":"mircea"})
print(response.status_code)

response = requests.post(URL+'/prieten', json={"nume":"irina"})
print(response.status_code)

response = requests.post(URL+'/prieten', json={"nume":"ana"})
print(response.status_code)

response = requests.get(URL+'/prieten?id=2')
print(response.json()["nume"])