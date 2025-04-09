import time
import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=36.2981&longitude=59.6057&hourly=temperature_2m'
params = {}
weather_date = requests.get(url).json()
print(weather_date['hourly']['temperature_2m'])



langs=['C#','Python','Java','Java','C','C#']
new_list=list(set(langs))
dicts=list(map(lambda x:(x,True),langs))
print(langs)
print(new_list)
print(dicts)
