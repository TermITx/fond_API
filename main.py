from typing import Union
import services as service
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add")
def plus_one(num: int):
    return {"Result": num + 1}

@app.get("/call_R_script")
def call_r_script(name : str):
    return service.call_R_script(name)

@app.get("/position")
def call_r_script(strategy: str):
    return service.get_position(strategy)

