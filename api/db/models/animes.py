from pydantic import BaseModel
from typing import Optional

class Anime(BaseModel):
    id: int
    image: str
    title: str
    episodes: Optional[int] = None
    status: str
    duration: str
    rating: str
    synopsis: str
    genres: list
    images: dict