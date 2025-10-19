from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import json
import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

class cat_obj(BaseModel):
    fact : str
    length : int



class User(BaseModel):
    email : str
    name : str
    stack : str

class InfoModel(BaseModel):
    status : str
    timestamp : str
    user:User
    fact : str

@app.get('/', response_model= InfoModel)
def get_my_stack_info():
    try:
        url = 'https://catfact.ninja/fact'
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch cat fact")
        
        data = response.json()
        fact = data.get("fact", "No fact found")
    except requests.Timeout:
        raise HTTPException(status_code=504, detail="Request to catfact.ninja timed out")
    except requests.ConnectionError:
        raise HTTPException(status_code=502, detail="Connection error occurred")
    except requests.exceptions.MissingSchema:
        raise HTTPException(status_code=400, detail="url required")

    user = User(
        email = 'okoh.onyeka123@gmail.com',
        name = 'Okoh emmanuel',
        stack = 'fastapi/ .net'
    )

    result = InfoModel(
        status="Success",
        timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        user=user,
        fact=fact
    )
    return result







