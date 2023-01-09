#python
from typing import Optional

#pydantic
from pydantic import BaseModel
#FASTAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path
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
        max_length=50,
        title="Person Name",
        description="This is the person name, It's between 1 and 50 characters"
    ),

    # El ... para hacerlo obligatorio, no recomendado en un Query parameter
    age: int = Query(
        ...,
        title="Person Age",
        description="This is the person Age. It's required"
        )
):
    return {name: age }

#validations: path parameters
@app.get("/person/detail/{person_id}")
def show_users(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person Id for the BD",
        description="This the person Id. It's required"
        )
    
):
    return {person_id: "It exist!"}
    