from pydantic import BaseModel


class UserCreate(BaseModel): #post
    name:  str
    email: str
    age:int


class UserUpdate(BaseModel):  #put
    name: str
    email: str
    age:int

class UserDelete(BaseModel):#delete
    name: str
    email: str

class UserResponse(UserCreate):  #get
    id:  int
    age: int | None = None

    class Config:
        # orm_mode = True   #allow data from orm
        from_attributes = True