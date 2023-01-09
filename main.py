#python
from typing import Optional

#pydantic
from pydantic import BaseModel
#FASTAPI
from fastapi import FastAPI
from fastapi import Body, Query
app = FastAPI()

#Models
class Person(BaseModel):
    first_name:str
    last_name:str
    age:int
    hair_color:Optional[str]=None
    is_married:Optional[bool]=None


@app.get("/")
def home():
    return {"Hello": "World"}

# Request and response body

@app.post("/person/new")
def create_person(person:Person=Body(...)):
    return person

#Validations:query parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        default=None,
        min_length=1,
        max_length=50
    ),

    # El ... para hacerlo obligatorio, no recomendado en un Query parameter
    age: int = Query(...)
):
    return {name: age }