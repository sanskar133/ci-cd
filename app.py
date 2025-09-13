
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class item(BaseModel):
    weight: int
    height: float

@app.get('/')
def read_root():
    return {'message': 'Hello i give bmi'}
@app.post('/obesity')
def calculate_obesity(Item:item):
    if Item.weight/(Item.height**2)<19:
        return {'status':'underweight'}
    elif Item.weight/(Item.height**2)<25:
        return {'status':'healthy'}
    else:
        return {'status':'overweight'}
