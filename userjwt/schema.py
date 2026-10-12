from pydantic import BaseModel


class UserCreate(BaseModel): #post
    username:str
    password:str
    role:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username: str | None = None

class UserOut(BaseModel):
    id:int
    username:str
    role: str
    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    username: str

    class Config:
        from_attributes = True