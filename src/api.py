from abc import ABC, abstractmethod
import requests
from models import Movie

key = open("data/apikey.txt").read()

class API(ABC):

    def get_movie_from_id(imdbid:str) -> Movie:
        data = requests.get("http://www.omdbapi.com/?i=" + imdbid + "&apikey=" + key).json()
        return Movie.from_dict(data)

    def get_movie_from_title(title:str, year:int) -> Movie:
        raise NotImplementedError("TODO")