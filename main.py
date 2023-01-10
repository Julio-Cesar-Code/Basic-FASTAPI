#python
from typing import Optional
from enum import Enum

#pydantic
from pydantic import BaseModel, Field
#FASTAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path
app = FastAPI()

class hairColor(Enum):
    white = "white"
    brown= "brow"
    black= "black"
    blonde= "blonde"
    red = "red"


#Models
class Location (BaseModel):
    city: str
    state: str
    country:str

class Person(BaseModel):
    first_name:str =Field(
        ..., 
        min_length=1,
        max_length=50
        )
    last_name:str = Field (
        ..., 
        min_length=1,
        max_length=50
        )
    
    age:int = Field(
        ...,
        gt=0,
        le=115
    )
    hair_color:Optional[hairColor]= Field( default=None)
    is_married:Optional[bool]=Field( default=None)


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


# Validation: Request Body

# Validations: Request Body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0
    ),
    person : Person = Body(...),
    location: Location= Body(...)

):
    result =person.dict()
    result.update(location.dict())
    return dict(person)