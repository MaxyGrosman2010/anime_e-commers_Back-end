import json
import requests

async def anime_get_all():
    response = requests.get('https://api.jikan.moe/v4/anime')
    dict_response = json.loads(response.text)

    animes = []
    for i in dict_response["data"]:
        animes.append(i)

    return animes