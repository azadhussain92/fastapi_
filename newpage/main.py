from fastapi import FastAPI,Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()
app.mount('/static',StaticFiles(directory="static"),name='static')
templates = Jinja2Templates(directory='templates')

@app.get('/')
def mydetails():
    return FileResponse("templates/index.html")
    
# @app.get('/',response_class=HTMLResponse)
# def mydetails(request:Request):
#     return templates.TemplateResponse(
#         request=request,name='index.html',
#         context={
#             "title": "home page",
#             "message": "Welcome to home page in fastapi..!"
#         }
#     )