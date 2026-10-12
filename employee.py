from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def employee():
    return[
        "Welcome To Employee Sheet",
        {
            "id": 1,
            "emp_name":"azad hussain",
            "age":24,
            "course":"python full stack with data science"
        },
        {
            "id":2,
            "name":"gaurav kumar",
            "Age": 25,
            "course":"data science"
        },
        {
            "id":3,
            'name':"amrit raj",
            "age":24,
            "course":"java full stack",
        },
        {
            "id":4,
            "name":"sanchy kumar",
            "age":25,
            "course":"data science"
        },
        {
            "id":5,
            "name":"yogesh kumar",
            "age":25,
            "course":"data analytics",
        }
    ]

# @app.post("/employee")
# def create_student(employee:dict):
#     employee.append(employee)
#     return{
#         "message":"employee create successfullu",
#         "employee":employee
#     }
