# from database import SessionLocal
# import schema
# import models

# def create_USER(db: schema,
#                 USER: schema.UserCreateCreate):
#     db_user = models.User(
#         title = USER.title,
#         description = USER.description,
#         priority = USER.priority,
#         completed = USER.completed
#     )

#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user