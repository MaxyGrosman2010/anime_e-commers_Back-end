from fastapi import APIRouter, status, HTTPException
import json
import requests
from db.models.animes import Anime
from db.models.episode import Episode
from db.schemas.animes import schema_anime, schema_animes
from db.schemas.episode import schema_episodes

router = APIRouter(prefix= "/animes", tags=["animes"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})

@router.get('', response_model= dict)
async def per_page(page: int):
    response = requests.get(f'https://api.jikan.moe/v4/anime?page={page}&&sfw=true&&type=tv')
    dict_response = json.loads(response.text)
    batch_animes = schema_animes(dict_response["data"])
    last_page = dict_response["pagination"]["last_visible_page"]
    return {"last_page": last_page ,"animes": batch_animes}


@router.get('/{id}', response_model= Anime)
async def by_id(id: int):
    try:
        response = requests.get(f'https://api.jikan.moe/v4/anime/{id}')
        dict_response = json.loads(response.text)
        return Anime(**schema_anime(dict_response["data"]))
    except: raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
    detail={"message": "The anime doesn't exist"})

@router.get('/{id}/episodes')
async def episodes(id: int, response_model= list):
    try:
        response = requests.get(f'https://api.jikan.moe/v4/anime/{id}/videos')
        dict_response = json.loads(response.text)
        return schema_episodes(dict_response["data"]["episodes"])
    except: raise HTTPException(status.HTTP_404_NOT_FOUND,
        {"message": "The anime doesn't have episodes"})
    
@router.get('/{id}/episodes/{episode}')
async def episode(id: int, episode: int, response_model = Episode):
    try:
        response = requests.get(f'https://api.jikan.moe/v4/anime/{id}/videos')
        dict_response = json.loads(response.text)
        list_episodes = schema_episodes(dict_response["data"]["episodes"])
        for element in list_episodes:
            print(element["id"], episode)
            if element["id"] == episode: return Episode(**element)
    except: raise HTTPException(status.HTTP_404_NOT_FOUND,
        {"message": "The anime doesn't have episodes"})