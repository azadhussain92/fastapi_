from fastapi import FastAPI,Body

app = FastAPI()

STUDENT = [
    {
      'Id':1,'Name': 'Azad Hussain','Degree': 'BE','Stream': 'CS','Marks': 65,'Address': 'Bangalor','Yop': 2025,'Skills': ['C++', 'Python', 'DSA'],'Certification': ['Python', 'AWS','WebTech','Deloitte']
    },
    {
        'Id':2,'Name': 'Amrit','Degree': 'IT','Stream': 'IS','Marks': 60,'Address': 'Bangalor','Yop': 2025,'Skills': ['C', 'Java', 'DSA'],'Certification': ['Python', 'AWS', 'Java']
    },
    {
        'Id':3,'Name': 'Yogesh','Degree': 'Mech','Stream': 'DS','Marks': 70,'Address': 'Bangalor','Yop': 2025,'Skills': ['c#', 'Python'],'Certification': ['Python', 'AWS']
    },
    {
        'Id':4,'Name': 'Hussain','Degree': 'B.TECH','Stream': 'CSE','Marks': 70,'Address': 'Bangalor','Yop': 2026,'Skills': ['.NET','WEBTECH'],'Certification': ['Python', 'WebTech']
    },
    {
       'Id':5, 'Name': 'Gaurav Kumar','Degree': 'BE','Stream': 'CS','Marks': 63,'Address': 'Bangalor','Yop': 2025,'Skills': ['Django','.NET','WEBTECH','ReactJs'],'Certification': ['Python', 'WebTech','Google']
    },
    {
       'Id':6, 'Name': 'Md Shakil','Degree': 'BE','Stream': 'CSE-DS','Marks': 67,'Address': 'Noida','Yop': 2025,'Skills': ['Python'],'Certification': ['Python','Data Science']
    }
]

@app.get('/')
def first():
    return{'meessage':'Welcome to Fastapi'}

@app.get('/get')
def student():
    return STUDENT

# @app.get('/{dynamic_parametar}')
# def  newfunction(dynamic_parametar):
#     return {'message':dynamic_parametar}


@app.get('/{Stream}')
def stud_info(Stream):
    res =[]
    for std in STUDENT:
        if std['Stream'].casefold()== Stream.casefold():
            res.append(std)
    return res

# fetch the student whose year is 2026 and skill set python 

@app.get("/Yop/{Yop}")
def stud_info(Yop:int):
    res = []
    for std in STUDENT:
        if std['Yop'] == 2026:
            res.append(std)
    return res

@app.get('//{skill}')
def stud_skill(skill):
    res = []
    for std in STUDENT:
        if 'python' in [s.casefold() for s in std['Skills']]:
            res.append(std)
    return res


@app.post("/addnewstd")
def add_Student(new_std=Body()):
    STUDENT.append(new_std)
    # return "Student Added Successfull.."

@app.put("/editstd/{stdid}")
def edit_student(stdid:int,modifyinfo=Body()):
    for std in range(len(STUDENT)):
        if STUDENT[std].get('Id') == stdid:
            STUDENT[std] = modifyinfo
            return "Record Updated Successfully"
    return "no id  exist"


@app.delete("/delete/{stdid}")
def delete_student(stdid:int):
    for std in range(len(STUDENT)):
        STUDENT.pop(std)
        return "Record Deleted Successfully"
    return " no id exist"

