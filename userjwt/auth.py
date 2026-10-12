from passlib.context import CryptContext
import bcrypt
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from datetime import datetime,timedelta,timezone
from fastapi.security import OAuth2PasswordBearer
import models,schema
from jose import JWTError,jwt
from database import get_db

SECRET_KEY ="QvWFb66o_TqSI3RwvqbwjqO-NYc3MTd56URt5rO7YKQ"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(
    schemes=["bcrypt"],deprecated="auto"
)

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")

def verify_password(plain_password: str ,hash_password:str) -> bool:
    return pwd_context.verify(plain_password,hash_password)

def get_user(db:Session,username:str):
    return db.query(models.User).filter(models.User.username== username).first()

def authenticate_user(db:Session,username:str,password:str):
    user = get_user(db,username)
    if not user or not  verify_password(password,user.password):
        return False
    return user

def create_access_token(data:dict,expires_delta:timedelta | None = None) ->str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+(expires_delta or timedelta(minutes=15))
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

def get_current_users(
        token:str = Depends(oauth2_scheme),
        db:Session= Depends(get_db)
):
    credentials_expception =HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        # headers={"WWW-Authenticate":"Bearer"}
    )
    try:
        payload =jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        username:str =payload.get("sub")
        if username is None:
            raise credentials_expception
        token_data = schema.TokenData(username=username)
    except JWTError:
        raise credentials_expception

    user =get_user(db,username=token_data.username)
    if user is None:
        raise credentials_expception
    return user
