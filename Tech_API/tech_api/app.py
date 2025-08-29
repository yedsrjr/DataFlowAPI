from fastapi import FastAPI

from tech_api.routers import animals, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(animals.router)
