from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"],
    responses={404: {"message": "Not found"}})