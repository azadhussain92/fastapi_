from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from models import User
import models
from database import engine, SessionLocal
import schema,qry

app =FastAPI()

#create tables automatically
models.Base.metadata.create_all(bind=engine)

#dependency open & close DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#display all the record in database table
@app.get('/users/',response_model=list[schema.UserResponse])
def get_users(db: Session = Depends(get_db)):
     return db.query(models.User).all()

#to fetch the single record in database table
@app.get('/users/{user_id}',response_model=schema.UserResponse)
def get_by_id(user_id:int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User Not Found")
    return user

#to add  new user record
@app.post('/add/users',response_model=schema.UserResponse)
def create_user(user: schema.UserCreate,db:Session=Depends(get_db)):
    db_user = models.User(name=user.name,email=user.email,age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#display the student details whose name starting with given input character in like that (a or A)

@app.get('/users/name/{user_name}')
def find_name(user_name:str,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.name.like(f"{user_name}%")).all()
    if not user:
        raise HTTPException(status_code=404,detail="user not find")
    return user


#modify the existing record
@app.put('/edituser/{user_id}',response_model=schema.UserResponse)
def update_user(user_id:int, user_data:schema.UserUpdate,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="user not found")

    user.email =user_data.email
    user.name = user_data.name
    user.age = user_data.age
    db.commit()
    db.refresh(user)
    return user

#delete the existing record
@app.delete('/userdelete/{user_id}',response_model=schema.UserResponse)
def delete_user(user_id:int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="user not found")
    db.delete(user)
    db.commit()
    return{"message": "Usere Delete Successfully"}
