import json
# pip install requests
import requests
import pandas as pd

url = requests.get("https://analytics.usa.gov/data/live/realtime.json")
text = url.text
# print(type(text))
data = json.loads(text)
# print(type(data))
# print(data)
df = pd.DataFrame(list(data.items()), columns=['Index', 'Value(s)'])
print(df)
