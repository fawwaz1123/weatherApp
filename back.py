from fastapi import FastAPI
from pydantic import BaseModel
from requests import get
from fastapi.middleware.cors import CORSMiddleware
import os
app = FastAPI()

origins = ["http://127.0.0.1:5500"]
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)
@app.get("/weather")
async def get_weather(city: str,units: str):
    temp = get("http://api.openweathermap.org/data/2.5/weather?APPID="+os.environ.get('weatherID')+"&q="+city+"&units="+units)
    data = temp.json()
    return data


