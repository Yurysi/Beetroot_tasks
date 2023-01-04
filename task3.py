import requests

"""
The Weather app

Write a console application which takes as an input a city name and returns 
current weather in the format of your choice. For the current task, you can 
choose any weather API or website or use openweathermap.org 
"""
import requests

user_city = input("Enter your city: ")
user_country = input("Enter your country: ")


def wheather(city, country):
    base_url = f"http://api.weatherstack.com/current?access_key=4f7cf8aa2e7d537c6c8d51e800607187&query={city},{country}"
    params = {
        "access_site": "4f7cf8aa2e7d537c6c8d51e800607187",
        'access_key': 'fanker1997@gmail.com',
        'query': 'qwerty1997'
    }
    response = requests.get(base_url)
    result = response.json()
    print('\n', result['request']['query'])
    for key, value in result['current'].items():
        if key != 'weather_icons':
            print(key, ' : ', value)


if __name__ == '__main__':
    wheather(user_city, user_country)

