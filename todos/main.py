from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from models import USER
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
@app.get('/todos/',response_model=list[schema.UserResponse])
def get_todos(db: Session = Depends(get_db)):
     return db.query(models.USER).all()

#to add  new user record
@app.post('/add/todos',response_model=schema.UserResponse)
def create_todos(USER: schema.UserCreate,db:Session=Depends(get_db)):
    db_user = models.USER(title=USER.title,description=USER.description,priority=USER.priority,completed=USER.completed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#to fetch the single record in database in table
@app.get('/todos/{todos_id}')
def todos_by_id(todos_id:int,db:Session=Depends(get_db)):
    todos = db.query(models.USER).filter(models.USER.id==todos_id).first()
    if USER is None:
        raise HTTPException(status_code=404,detail="User Not Found")
    return todos


#display the record using periority
@app.get('/todos/{priority_name}')
def todos_priority(priority_name:str,db:Session=Depends(get_db)):
    todos = db.query(models.USER).filter(models.USER.priority==priority_name).first()
    if not todos:
        raise HTTPException(status_code=404,detail="User Not Found")
    return todos

#modify the existing record
@app.put('/edittodos/{todos_id}')
def update_todos(todos_id:int,user_data:schema.UserUpdate,db:Session=Depends(get_db)):
    USER = db.query(models.USER).filter(models.USER.id==todos_id).first()
    if USER is None:
        raise HTTPException(status_code=404,detail="User not found")
    USER.title = user_data.title
    USER.description = user_data.description
    USER.priority = user_data.priority
    USER.completed = user_data.completed
    db.commit()
    db.refresh(USER)
    return USER

#delete the existing record
@app.delete('/todosdelete/{todos_id}')
def delete_todos(todos_id:int,db:Session=Depends(get_db)):
    USER = db.query(models.USER).filter(models.USER.id==todos_id).first()
    if USER is None:
        raise HTTPException(status_code=404,detail="User Not Found")
    db.delete(USER)
    db.commit()
    return{"message": "User delete Successful"}