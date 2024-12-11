from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import uvicorn
from mylib.bot import scrape
from pydantic import BaseModel

app = FastAPI()

# class Wiki(BaseModel):
#     name: str

# @app.post('/predict')
# async def predict_story(wiki: Wiki):
#     result = scrape(name=wiki.name)
#     payload = {"wikipage": result }
#     json_compatable_item_data = jsonable_encoder(payload)
#     return JSONResponse(content=json_compatable_item_data)

@app.get('/')
async def root():
    return {"message": "Hello world!"}

# @app.get('/add/{num1}/{num2}')
# async def add(num1:int, num2:int):
#     total = num1 + num2
#     return {"total": total}
