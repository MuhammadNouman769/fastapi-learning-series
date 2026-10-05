

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def home():
    return {"message":"hello with venv"}

@app.get("/about")
def about():
    return {"message":"about page"}    

@app.get("/about/users")
def users():
    return {"name":"Nouman",
            "roll":"backend"
        }

@app.get("/users/{user_id:int}")
def get_user(user_id):
    return {"user_id":user_id}


@app.get("/users")
def get_user(name: str = None):
    return {"name":name}


@app.get("/products")
def get_user(limit: int = 10):
    return {"limit":limit}    


@app.get("/items")
def get_user(name: str = None, price: int = 0):
    return {
            "name":name,
            "price":price,
            }    
class User(BaseModel):
    name:str
    age:int
@app.post("/create_user")
def create_user(user:User):
    return{
        "message":"user created",
        "data":user
    }


@app.put("/users/{user_id}")
def updated_user(user_id:int,user:User,notify:bool = False):
    if user_id < len(users):
        users[user_id]=user

        return {
            "message":"User Updated",
            "notify":"notify",
            "data":user
        }
    return {
        "error":"User not fount"
    }
