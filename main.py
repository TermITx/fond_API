from typing import Union
import services as service
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/",response_class=HTMLResponse)
async def read_root():
    
    return """
<html>
    <head>
        <!-- head definitions go here -->
    </head>
    <body>
        <h1> Let's make some money! </h1>
    </body>
</html>
"""
@app.get("/add")
def plus_one(num: int):
    return {"Result": num + 1}

@app.get("/call_R_script")
def call_r_script(name : str):
    return service.call_R_script(name)

@app.get("/position")
def call_r_script(strategy: str):
    return service.get_position(strategy)

