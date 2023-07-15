#RTM: https://rapidapi.com/darkskyapis/api/dark-sky/
import requests

url = "https://dark-sky.p.rapidapi.com/%7Blatitude%7D,%7Blongitude%7D"

querystring = {"units": "auto", "lang": "en"}

headers = {
    "X-RapidAPI-Key": "719758a469mshc3ecae83f1cbef6p16e435jsn3c03c9cb21c5",
    "X-RapidAPI-Host": "dark-sky.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())