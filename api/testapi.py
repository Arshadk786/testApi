from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI()


class Text(BaseModel):
    text : str

@app.get("/")
async def index():
    return {"message": "Welcome to the API"}

@app.post("/test")
async def predict(request : Text):
    return request