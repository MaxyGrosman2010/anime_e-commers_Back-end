import json
import requests

async def anime_get_all():
    response = requests.get('https://api.jikan.moe/v4/anime')
    dict_response = json.loads(response.text)