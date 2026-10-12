from sqlalchemy import Column, Integer, String,Boolean
from database import Base

class USER(Base):
    __tablename__ ="mytodos"

    id    = Column(Integer, primary_key =True,index=True)
    title = Column(String(100))
    description = Column(String(100))
    priority = Column(String(100))
    completed = Column(Boolean,default=False)
    