from fastapi import FastAPI
from scraper import Hamrorashifal

data = Hamrorashifal

app = FastAPI()
@app.get("/")
async def dailyrashifal():
   return data.scraperashifal(data)