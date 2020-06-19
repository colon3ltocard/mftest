"""
Main module for our mftest app
"""
from fastapi import FastAPI

from mftest.omdb import get_movies
from mftest.schemas import Movie

app = FastAPI()


@app.post("/foobar")
def foorbar_endpoint(movie: Movie):
    """
    This url is a proxy to omdbapi.
    :return:
    """
    print(movie)
    return get_movies(**movie.dict())

