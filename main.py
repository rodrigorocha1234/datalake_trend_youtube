from src.config.config import Config
import requests

url = "https://youtube.googleapis.com/youtube/v3/videos"

params = {
    "part": "statistics,contentDetails,snippet",
    "chart": "mostPopular",
    "maxResults": 50,
    "regionCode": "BR",
    "key": Config.CHAVE_API_YOUTUBE
}

r = requests.get(url, params=params)
print(r.status_code)
