from pydantic import BaseModel


class UserCreate(BaseModel): #post
    title:str
    description:str
    priority:str
    completed:bool


class UserUpdate(BaseModel):  #put
    title:str
    description:str
    priority:str
    completed:bool

class UserDelete(BaseModel):#delete
    title:str
    description:str
    priority:str
    completed:bool

class UserResponse(UserCreate):  #get
    id:  int

    class Config:
        orm_mode = True   #allow data from orm
        from_attributes = True