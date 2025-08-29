from http import HTTPStatus

from fastapi import FastAPI

from tech_api.routers import animals, auth, users
from tech_api.schemas import Message

app = FastAPI()

app.include_router(auth.router)
app.include_router(animals.router)
app.include_router(users.router)


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Bem vindo a API"}
