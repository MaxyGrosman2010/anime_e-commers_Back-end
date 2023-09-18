from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import animes, users

app = FastAPI()

# origins = []
# 
# app.add_middleware(CORSMiddleware, allow_credentials = True, allow_method = ["*"],
#     allow_headers = ["*"])
app.include_router(router= animes.router)
app.include_router(router= users.router)