import sqlite3 as sql
from models import Movie

class MovieDb:
    def __init__(self, path:str) -> None:
        self.connection: sql.Connection = sql.connect(path)
        self.setup()

    def setup(self) -> None:
        self.connection.executescript(open("src/SQL/setup.sql").read())

    def add(self, movie:Movie) -> None:
        if self.connection.execute("SELECT * FROM movie WHERE imdbid = ?", (movie.imdbid,)).fetchone() != None:
            self.update(movie)
            return
        self.connection.execute(open("src/SQL/add_movie.sql").read(), movie.as_tuple())
        self.connection.commit()
    
    def update(self, movie:Movie) -> None:
        if self.connection.execute("SELECT * FROM movie WHERE imdbid = ?", (movie.imdbid,)).fetchone() == None:
            self.add(movie)
            return
        self.connection.execute("UPDATE movie SET title= ?, year= ? WHERE imdbid= ?", (movie.title, movie.year, movie.imdbid))

    def get_alphabetical(self):
        result = []
        for row in self.connection.execute("SELECT * FROM movie ORDER BY title"):
            movie = Movie.from_tuple(row)
            result.append(movie)
        return result

    def close(self) -> None:
        self.connection.close()
        