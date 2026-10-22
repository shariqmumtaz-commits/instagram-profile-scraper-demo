from fastapi import FastAPI
from scraper import run_scraper

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Instagram Profile Scraper API is running"
    }


@app.get("/scrape")
def scrape(username: str):
    return run_scraper(username)