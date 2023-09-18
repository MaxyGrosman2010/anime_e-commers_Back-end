from api.controller.get_all_animes import anime_get_all
import json
import requests

_all_animes = []

def all_animes():
    i = 1
    response = requests.get(f'https://api.jikan.moe/v4/anime?page={i}')
    dict_response = json.loads(response.text)

    print(dict_response["pagination"]["has_next_page"])
    # while dict_response["pagination"]["has_next_page"]:
    #     batch_animes = anime_get_all(dict_response["data"])
