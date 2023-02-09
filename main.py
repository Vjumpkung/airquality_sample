from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/temperature/log")
def get_temp():
    with open("sample_temp.json") as fp:
        file = json.load(fp)
    return file


@app.get("/humidity/log")
def get_hum():
    with open("sample_hum.json") as fp:
        file = json.load(fp)
    return file


@app.get("/co/log")
def get_co():
    with open("sample_co.json") as fp:
        file = json.load(fp)
    return file


@app.get("/temperature")
def get_temp():
    with open("sample_temp.json") as fp:
        file = json.load(fp)
    return file[0]


@app.get("/humidity")
def get_hum():
    with open("sample_hum.json") as fp:
        file = json.load(fp)
    return file[0]


@app.get("/co")
def get_co():
    with open("sample_co.json") as fp:
        file = json.load(fp)
    return file[0]
