from fastapi import APIRouter, status, HTTPException
import json
import requests
from db.models.animes import Anime
from db.schemas.animes import schema_anime, schema_animes

router = APIRouter(prefix= "/animes", tags=["animes"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})
# response_model= dict
@router.get('')
async def per_page(page: int):
    response = requests.get(f'https://api.jikan.moe/v4/anime?page={page}&&sfw=true')
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
    detail={"message": "The id isn't valid"})