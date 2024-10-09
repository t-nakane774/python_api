from fastapi import FastAPI
import api.functions
from api import login

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Helloooo World"}
