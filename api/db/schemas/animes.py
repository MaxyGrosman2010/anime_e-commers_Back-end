def schema_anime(anime) -> dict:
    return {"id": anime["mal_id"], "image": anime["images"]["jpg"]["image_url"],
    "title": anime["title"], "episodes": anime["episodes"], "status": anime["status"],
    "duration": anime["duration"], "rating": anime["rating"], "synopsis": anime["synopsis"],
    "genres": anime["genres"], "images": anime["images"]["jpg"]}

def schema_animes(animes) -> list:
    return [schema_anime(anime) for anime in animes]