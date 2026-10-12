from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return{"message":"Hello Welcome To FastApi"}


# @app.get("/student")
# def student():
#     return{
#         "Name":"Azad Hussain",
#         "Age": 25,
#         "Year of PassOut": 2025,
#         "Treaning": "Pyspider",
#         "Location":"Bangalor",
#         "Stream":"Computer Science Engineering",
#         "Course":"Python Full Stack Developer",
#         "Main Focuse":"Python,DSA,Programming,Django,RestApi,FastApi,Sql,WebTech"
#     }

# @app.get("/Employee")
# def Employee():
#     return{
#         "Name":"azad hussain",
#         "Age": 25,
#         "Depatment":"Software developer",
#         "Company":"Accenture",
#         "Experience":"Fresher",
#         "Skill":"python, DSA, Django,RestApi_Framework,Sql,WebTech,Python Programming"
#     }

# @app.get('/product')
# def product():
#     return{
#         "Product_Name":"Laptop",
#         "Brand":"HP",
#         "Price": 59000,
#         "Category":"Electronic",
#         "Ram": "16GB",
#         "Storage":"516GB",
#         "Processor":"AMD RYZEN 5",
#         "Stock":"Availavle"
#     }
