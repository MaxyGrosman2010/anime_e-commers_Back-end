from fastapi import APIRouter, status, HTTPException
import json
import requests
from db.models.animes import Anime, EpisodeDetail
from db.schemas.animes import schema_anime, schema_animes, schema_episodes
from db.schemas.animes import schema_episode_detail

router = APIRouter(prefix= "/animes", tags=["animes"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})

@router.get('', response_model= dict)
async def per_page(page: int):
    response = requests.get(f'https://api.jikan.moe/v4/anime?page={page}')
    dict_response = json.loads(response.text)
    batch_animes = schema_animes(dict_response["data"])
    max_pages = dict_response["pagination"]["last_visible_page"]
    return {"animes": batch_animes, "last_page": max_pages}


@router.get('/{id}', response_model= Anime)
async def by_id(id: int):
    try:
        response = requests.get(f'https://api.jikan.moe/v4/anime/{id}')
        dict_response = json.loads(response.text)
        return Anime(**schema_anime(dict_response["data"]))
    except: raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
    detail={"message": "The id isn't valid"})

@router.get('/{id}/episodes', response_model= dict)
async def episodes_by_anime(id: int):
    response = requests.get(f'https://api.jikan.moe/v4/anime/{id}/episodes')
    dict_response = json.loads(response.text)
    batch_episodes = schema_episodes(dict_response["data"])
    last_page = dict_response["pagination"]["last_visible_page"]

    return {"episodes": batch_episodes, "last_page": last_page}

@router.get('/{id}/episodes/{episode}')
async def episode_by_id(id: int, episode: int):
    response = requests.get(f'https://api.jikan.moe/v4/anime/{id}/episodes/{episode}')
    dict_response = json.loads(response.text)

    try: return EpisodeDetail(**schema_episode_detail(dict_response["data"]))
    except: raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
    detail={"message": "This episode doesn't exist"})