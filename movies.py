from fastapi import FastAPI,Body,Path
from pydantic import BaseModel,Field


app = FastAPI()

class MOVIES :
    id:str
    title:str
    director:str
    duration:int
    certificate:str
    genre:str
    language:str
    cast:str
    budget:int
    collection:int
    year:int
    rating:int

class MOVIES :
    def __init__(self,id,title,director,duration,certificate,genre,language,cast,budget,collection,year,rating):

        self.id=id
        self.title=title
        self.director=director
        self.duration=duration
        self.certificate=certificate
        self.genre=genre
        self.language=language
        self.cast=cast
        self.budget=budget
        self.collection=collection
        self.year=year
        self.rating=rating

class moviesrequest(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length=3)
    director: str
    duration: float
    certificate: str
    genre: str
    language: str
    cast: str
    budget: int
    collection: int
    year: int
    rating: int

allMovies = [
    MOVIES(1,'paradies','srikant',3,'A','drama','telugu','nani',200,300,2026,4),
    MOVIES(2,'kgf','prasant nil',3.5,'A','action','kanada','yesh',125,1250,2024,7),
]
@app.get('/')
def movies_review():
    return allMovies

#all movies in director in given in year

@app.get("/director/{year}")
def director_yer(year:int):
    movie = []
    for  movies in allMovies:
        if movies.year== year:
            movie.append(movies)
    return movie


@app.post('/add_movies')
def addnewmovies(movies_request: moviesrequest):
    newmovies = MOVIES(**movies_request.model_dump())
    allMovies.append(newmovies)
    return newmovies

def get_new_id(movie:MOVIES):

    lastID=allMovies[-1].id
    if lastID!=0:
        movie.id=lastID+1
    else:
        movie.id=1
    return movie

@app.get('/get_movie_year/{from_year}/{to_year}')
def get_movie_year(from_year:int=Path(gt=1990,lt=2026),to_year:int=Path(gt=1990,lt=2027)):
    mvs=[]
    for mv in allMovies:
        if mv.year>=from_year and mv.year<=to_year:
            mvs.append(mv)
    return mvs

@app.get('/get_movie_by_rating/{rating}')
def get_movie_by_rating(rating:int=Path(gt=0,lt=11)):
    mvs=[]
    for mv in allMovies:
        if mv.rating == rating:
            mvs.append(mv)
    return mvs

@app.put('/edit/movies')
def edit_movies(movies:moviesrequest):
    for i in range(len(allMovies)):
        if movies.id == allMovies[i].id:
            allMovies[i]= movies
            return "movies updated"

@app.delete('/delet_movies/{id}')
def delet_movies(id:int):
    for i in range(len(allMovies)):
        if allMovies[i].id == id:
            allMovies.pop(i)
        return "movies deleted successfully.."