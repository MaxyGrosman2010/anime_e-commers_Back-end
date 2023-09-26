from pydantic import BaseModel

class Episode(BaseModel):
    id: int
    name: str
    image: str