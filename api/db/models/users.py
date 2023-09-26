from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    name: str
    surname: str
    username: str
    age: int
    email: str
    favorites: Optional[list] = None
    bought: Optional[list] = None
    expire_date_animes: Optional[list] = None

class UserDB(User):
    password: str
    disable: Optional[bool] = False