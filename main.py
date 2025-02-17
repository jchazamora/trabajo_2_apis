from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

database = []

class User(BaseModel):
    name: str
    password: str

@app.post("/user")
def create_user(user: User):
    database.append(user)
    return ("Usuario creado exitosamente")

@app.get("/user")
def read_user():
    if not database:
        raise HTTPException(status_code=404, detail="Usuario no existe")
    return database[0]
