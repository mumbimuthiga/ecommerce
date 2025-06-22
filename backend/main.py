from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id:int
    name:str
    age:int

DB:List[Person]=[
        Person(id=1, name="John Doe", age=30),
        Person(id=2, name="Jane Doe", age=25),
        Person(id=3, name="Alice Smith", age=28),
        Person(id=4, name="Bob Johnson", age=35)
    ] 
        


@app.get("/api", response_model=List[Person])
def read_root():
    return DB


