def schema_episode(episode)-> dict:
    return {"id": episode["mal_id"], "name": f'{episode["episode"]}: {episode["title"]}',
        "image": episode["images"]["jpg"]["image_url"]}

def schema_episodes(episodes) -> list:
    return [schema_episode(episode) for episode in episodes]