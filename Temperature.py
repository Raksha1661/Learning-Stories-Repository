import requests

def get_temperature(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        print(f"Current temperature in {city}: {temp}°C")
    else:
        print("Error:", data.get("message", "Unable to fetch temperature."))

# Example usage
city = input("Enter your city name: ")
api_key = "your_api_key_here"  # Replace with your actual API key
get_temperature(city, api_key)
