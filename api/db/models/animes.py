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
    images: dict