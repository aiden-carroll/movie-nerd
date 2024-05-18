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
            raise ValueError("Movie does not exist!")
        self.connection.execute("UPDATE movie SET title= ?, year= ? WHERE imdbid= ?", (movie.title, movie.year, movie.imdbid))
    
    def search_title(self, title:str="", order_col:str="title", descending:bool=False) -> list[Movie]:
        title = '%' + title + '%'
        if descending:
            rows = self.connection.execute("SELECT * FROM movie WHERE title LIKE ? ORDER BY ? DESC", (title, order_col)).fetchall()
        else:
            rows = self.connection.execute("SELECT * FROM movie WHERE title LIKE ? ORDER BY ? ASC", (title, order_col)).fetchall()
        result = []
        for row in rows:
            movie = Movie.from_tuple(row)
            result.append(movie)
        return result
    
    def close(self) -> None:
        self.connection.close()
        