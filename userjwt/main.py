from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session 
from models import User
import models
from database import engine, SessionLocal
import schema,auth
from auth import hash_password
from fastapi.security import OAuth2PasswordRequestForm 
from datetime import timedelta



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

#regester the function
@app.post("/regester")
def regester(user:schema.UserCreate,db:Session=Depends(get_db)):
    existing =db.query(models.User).filter(
        models.User.username == user.username
    ).first()
    if existing:
        raise HTTPException(400,"username already exists")
    new_user = models.User(
        username=user.username,
        password=hash_password(user.password),
        role= user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#display the message if user is exist or not
@app.get('/login/{user_name}',response_model=schema.UserResponse)
def login(user_name:str,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.username==user_name).first()
    if user is None:
        raise HTTPException(status_code=404,detail="user does not exist")
    return user

#login function 
@app.post("/login",response_model=schema.Token)
def login(
    from_data: OAuth2PasswordRequestForm = Depends(),
    db:Session = Depends(get_db)
):
    user  = auth.authenticate_user(db,from_data.username,from_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= 'incorrct usrname or password ',
            headers={ "WWW-Authenticate": "Bearer"},
    )
    access_token_expires = timedelta(
        minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = auth.create_access_token(
        data = {"sub": user.username},
        expires_delta=access_token_expires
    )
    return {
    "access_token": access_token,
    "token_type": "Bearer"
}

@app.get("/users/me",response_model=schema.UserOut)
def read_users_me(
    current_user:models.User = Depends(auth.get_current_users)
):
    return current_user