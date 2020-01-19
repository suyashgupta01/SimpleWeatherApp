import requests as rq
import json

class Weather():
    
    def __init__(self, city_name):
        self.city = city_name
        response = rq.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=873fb99f9ed6b2491a3ff4a5bd95285c")
        results = response.json()
        self.weather_disc = weather[0]['main']
        self.humidity = str(results['main']['humidity'])
        self.temp = results['main']['temp']
        self.temp = self.temp -273.15
        self.max_temp = results['main']['temp_max']
        self.max_temp = self.max_temp -273.15
        self.min_temp = results['main']['temp_min']
        self.min_temp = self.min_temp - 273.15
        
        
    def return_weather(self):
        return [self.weather_disc, str(self.temp) + " degree celcius" , str(self.max_temp) + " degree celcius" , str(self.min_temp) + " degree celcius" , str(self.humidity) + " percent"]
    

def main():
    city_name = input("Please enter city name:")
    x = Weather(city_name)
    mausam = x.return_weather()
    print("Weather in " + city_name + " is as follows: \n" + mausam[0] + "\nTemperature: " + mausam[1] + "\nMax Temperature: " + mausam[2] + "\nMin Temperature: " + mausam[3] + "\nHumidity: " + mausam[4] + "\n" )
    
    
main()
