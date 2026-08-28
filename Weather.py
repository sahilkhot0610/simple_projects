import requests

city = input("Enter the Name of City : ")
API_KEY = "599afe561c9cc14b208723139af4db25"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print("City : ", data["name"])
print("Temperature : ", data["main"]["temp"], "°C")
print("Humidity : ", data["main"]["humidity"])