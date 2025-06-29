
from typing import List
from uuid import uuid4,UUID
from fastapi import FastAPI,HTTPException
from models import User,Gender,Role

app=FastAPI()
db: List[User]=[
    User(
        id=uuid4(),
        first_name="Veny",
        last_name="Mumbi",
        middle_name="Mumbi",
        gender=Gender.female,
        roles=[Role.student],
    ),
     User(
        id=uuid4(),
        first_name="Man",
        last_name="Man2",
        middle_name="Mumbi",
        gender=Gender.male,
        roles=[Role.student,Role.user],
    )

]

@app.get('/')

async def root():
    return {"Hello" :"world"}


@app.get('/api/v1/users')

async def fetch_users():
    return db

@app.post('/api/v1/users')
async def register_users(user:User):
    db.append(user)
    return{"message":"user created successfully","user":user.id,"user_name":user.first_name}



@app.get('/api/v1/user/{user_id}')
async def get_user(user_id:UUID):
   
    for user in db:
        if user.id==user_id:
            return user   
    raise HTTPException(
        status_code=404,
        detail="User does not exist yet"
    )



@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return {"message":"user deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"User with id {user_id} does not exist"
        )
    # return {"message":"user not found"}



@app.put('/api/v1/users/{user_id}')
async def update_user(user_id:UUID):
    return "hry"
    