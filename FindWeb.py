# pip install requests
import requests


def url_ok(url_check):
    try:

        response = requests.head(url_check)

        if response.status_code == 200:
            return "True"
        else:
            return "False"
    except requests.ConnectionError as e:
        return e


url = "https://analytics.usa.gov/data/live/realtime.json"
print(url_ok(url))
