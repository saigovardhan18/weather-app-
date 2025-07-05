

API_KEY = "b1b15e88fa797225412429c1c50c122a1" 
city = input("enter you city name")

# Fetch weather data"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric" 
response = requests.get(url)
data = response.json()

# Extract temperature 
temp = data ['main']['temp']
print(f"current temperature in {city} : {temp} degrees celcius")