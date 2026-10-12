from database import SessionLocal
import schema
import models

def create_user(db: schema,
                user: schema.UserCreate):
    db_user = models.User(
        name = user.name,
        email =user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user