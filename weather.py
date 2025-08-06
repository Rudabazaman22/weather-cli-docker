import sys
import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print("Failed to get weather info")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
    else:
        get_weather(sys.argv[1])
