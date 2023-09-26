from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import os
from os.path import join, dirname
from dotenv import load_dotenv
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from db.models.users import UserDB, User
from db.schemas.users import userdb_schema, user_schema
from db.client import db_client

router = APIRouter(prefix="/users", tags=["users"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})
oauth2 = OAuth2PasswordBearer(tokenUrl="/login")
crypt = CryptContext(schemes=["bcrypt"])
dotenv_path = join(dirname(__file__), "env")
load_dotenv(dotenv_path)
ACCESS_TOKEN_DURATION = os.environ.get("ACCESS_TOKEN_DURATION")
SECRET = os.environ.get("SECRET")
ALGORITHM = os.environ.get("ALGORITHM")

def search_user(field: str, key):
    try: return UserDB(**userdb_schema(db_client.users.find_one({field: key})))
    except: return "Not found"

async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(status.HTTP_400_BAD_REQUEST, detail= "Invalid credentials")

    try:
        username = jwt.decode(token, SECRET, algorithms= ALGORITHM).get("sub")
        if username is None: raise exception
    except: raise exception

    return search_user("username", username)

async def current_user(user: UserDB = Depends(auth_user)):
    if user.disable: raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid user")

    return User(**user)

@router.post("/signUp")
async def sign_up(user: UserDB):
    if type(search_user("email", user.email)):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="This user already exist")
    
    password = crypt.hash(user.password)
    user_dict = dict(user)
    del user_dict["password"]
    user_dict["password"] = password
    id = db_client.anime_users.insert_one(user_dict).inserted_id

    return User(**user_schema(db_client.anime_users.find_one({"_id": id})))

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = search_user("username", form.username)
    if user_db == "Not found":
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail= "User isn't valid")
    if not crypt.verify(form.password, user_db.password):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Password isn't valid")
    if user_db.disable:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="This user was ban or it is inactive")
    
    access_token = {"sub": {user_db.username},
    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}
    return {"access_token": jwt.encode(access_token, SECRET, ALGORITHM),
    "token_type": "Bearer"}

@router.get('/profile')
async def me(user: User = Depends(current_user)):
    return User(**user)