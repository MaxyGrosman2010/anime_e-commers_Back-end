from fastapi import APIRouter, status, HTTPException
import json
import requests
from operator import attrgetter

router = APIRouter(prefix= "/animes", tags=["animes"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})

async def anime_get_all(all_animes):
    animes = []
    for i in all_animes:
        anime = i
        animes.append(anime)

    return animes

@router.get('/')
async def all():
    i = 1
    response = requests.get(f'https://api.jikan.moe/v4/anime?page={i}')
    dict_response = json.loads(response.text)
    
    while dict_response["pagination"]["has_next_page"]:
        batch_animes = anime_get_all(dict_response["data"])
    return batch_animes

@router.get('/{id}')
async def id(id: int):
    response = requests.get(f'https://api.jikan.moe/v4/anime/{id}')
    dict_response = json.loads(response.text)

    return dict_response