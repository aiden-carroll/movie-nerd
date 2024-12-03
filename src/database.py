import sqlite3 as sql
from models import Model, Movie

class Database:
    instance = {}
    sqlpath = ""

    def __init__(self, path:str) -> None:
        self.connection: sql.Connection = sql.connect(path)
        self.setup()

    def get_instance(path:str):
        if Database.instance:
            return Database.instance
        else:
            Database.instance = Database(path)
            return Database.instance

    def setup(self) -> None:
        pass

    def add(self, model:Model) -> None:
        if self.connection.execute("SELECT * FROM movie WHERE imdbid = ?", (movie.imdbid,)).fetchone() != None:
            raise ValueError("Movie already exists!")
        self.connection.execute(open("src/SQL/" + Database.sqlpath + "/add.sql").read(), model.as_dict())
        self.connection.commit()
    
    def update(self, model:Model) -> None:
        if self.connection.execute("SELECT * FROM movie WHERE imdbid = ?", (movie.imdbid,)).fetchone() == None:
            raise ValueError("Movie does not exist!")
        self.connection.execute(open("src/SQL/" + Database.sqlpath + "/update.sql"), model.as_dict())
    
    def close(self) -> None:
        self.connection.close()
        Database.instance = None

    def __del__(self):
        self.close()

class MovieDb(Database):
    instance = {}
    sqlpath = "movie"

    def setup(self) -> None:
        self.connection.executescript(open("src/SQL/movie_setup.sql").read())

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

    def search_director(self, director:str="", order_col:str="title", descending:bool=False) -> list[Movie]:
        director = '%' + director + '%'
        if descending:
            rows = self.connection.execute("SELECT * FROM movie WHERE director LIKE ? ORDER BY ? DESC", (director, order_col)).fetchall()
        else:
            rows = self.connection.execute("SELECT * FROM movie WHERE director LIKE ? ORDER BY ? ASC", (director, order_col)).fetchall()
        result = []
        for row in rows:
            movie = Movie.from_tuple(row)
            result.append(movie)
        return result

class ActorDb(Database):
    instance =  {}
    sqlpath = "actor"