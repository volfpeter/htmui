from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from holm import App

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

App(app=app)
