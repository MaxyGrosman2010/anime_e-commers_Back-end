#Animes
def schema_anime(anime) -> dict:
    return {"id": anime["mal_id"], "image": anime["images"]["jpg"]["image_url"],
    "title": anime["title"], "episodes": anime["episodes"], "status": anime["status"],
    "duration": anime["duration"], "rating": anime["rating"], "synopsis": anime["synopsis"],
    "genres": anime["genres"]}

def schema_animes(animes) -> list:
    return [schema_anime(anime) for anime in animes]
#Episodes
def schema_episode(episode) -> dict:
    return {"id": episode["mal_id"], "title": episode["title"]}

def schema_episodes(episodes):
    return [schema_episode(episode) for episode in episodes]

def schema_episode_detail(episode):
    return {"id": episode["mal_id"], "title": episode["title"],
    "duration": episode["duration"], "synopsis": episode["synopsis"]}