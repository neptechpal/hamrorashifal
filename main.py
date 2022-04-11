from fastapi import FastAPI
from scraper import Hamrorashifal, WeeklyRashifal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dailydata = Hamrorashifal
rashifaldata = WeeklyRashifal

rashilist = [
    "Mesh",
    "Brish",
    "Mithun",
    "Karkat",
    "Singha",
    "Kanya",
    "Tula",
    "Brischik",
    "Dhanu",
    "Makar",
    "Kumbha",
    "Meen"
]


@app.get("/")
async def dailyrashifal():
   return dailydata.scraperashifal(dailydata)

@app.get("/weekly")
async def weeklyrashifal():
   return rashifaldata.weeklyrashifal(rashifaldata,rashilist,"weekly")

@app.get("/monthly")
async def monthlyrashifal():
   return rashifaldata.weeklyrashifal(rashifaldata,rashilist,"monthly")

@app.get("/yearly")
async def yearlyrashifal():
   return rashifaldata.weeklyrashifal(rashifaldata,rashilist,"yearly")








