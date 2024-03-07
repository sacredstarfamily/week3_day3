import requests

base_url = "https://api.weatherapi.com/v1"
api_method = "/current.json"
api_key = "de736c53cea8444cbab205005240603"
city_name = "Mount Shasta"

request_url = f"{base_url}{api_method}?key={api_key}&q={city_name}"
res = requests.get(request_url)
weather_data = res.json()
print(request_url)
print(weather_data)
