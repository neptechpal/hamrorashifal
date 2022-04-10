from fastapi import FastAPI
from scraper import Hamrorashifal, WeeklyRashifal

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

app = FastAPI()
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

# list = [
#     "weekly",
#     "monthly",
#     "yearly"
# ]






