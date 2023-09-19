from pydantic import BaseModel

class Anime(BaseModel):
    id: int
    image: str
    title: str
    episodes: int
    status: str
    duration: str
    rating: str
    synopsis: str
    genres: list

class Episode(BaseModel):
    id: int
    title: str

class EpisodeDetail(Episode):
    duration: int
    synopsis: str