import datetime

class Model:

    def from_dict():
        pass

    def from_tuple():
        pass

    def as_tuple():
        pass

    def as_dict():
        pass

class Movie:
    def __init__(self, imdbid:int) -> None:
        self.set_imdbid(imdbid)
        self.title = None
        self.year = None
        self.score = None
    
    def from_dict(data: dict):
        movie = Movie(data["imdbID"])
        movie.set_title(data["Title"])
        movie.set_year(int(data["Year"]))
        movie.set_runtime(data["Runtime"])
        movie.set_rating(data["Rated"])
        movie.set_genre(data["Genre"])
        movie.set_director(data["Director"])
        movie.set_writer(data["Writer"])
        movie.set_actors(data["Actors"])
        movie.set_plot(data["Plot"])
        return movie

    def from_tuple(_tuple):
        movie = Movie(_tuple[0])
        movie.set_title(_tuple[1])
        movie.set_year(int(_tuple[2]))
        movie.set_rating(_tuple[3])
        movie.set_runtime(_tuple[4])
        movie.set_genre(_tuple[5])
        movie.set_director(_tuple[6])
        movie.set_writer(_tuple[7])
        movie.set_actors(_tuple[8])
        movie.set_plot(_tuple[9])
        movie.set_score(_tuple[10])
        return movie
    
    def set_imdbid(self, imdbid:str):
        if len(imdbid) > 10:
            raise ValueError("imdbid can't be longer than 10 characters!")
        if imdbid[:2] != "tt":
            raise ValueError("imdbid must start with 'tt'!")
        self.imdbid:int = imdbid

    def set_title(self, title:str) -> None:
        if len(title) > 255:
            raise ValueError("Name can't be longer than 255 characters!")
        self.title = title
        
    def set_year(self, year:int):
        if year < 0:
            raise ValueError("Year cannot be negative!")
        if year > 9999:
            raise ValueError("Year must be a 4 digit number!")
        self.year:int = year
    
    def set_runtime(self, runtime) -> None:
        if len(runtime) > 255:
            raise ValueError("Runtime can't be longer than 255 characters!")
        self.runtime:str = runtime
    
    def set_rating(self, rating:str) -> None:
        if not rating in ['G', 'PG', 'PG-13', 'R', 'NC-17', 'NR']:
            raise ValueError("Rating must be a valid rating!")
        self.rating:str = rating
    
    def set_genre(self, genre:str) -> None:
        self.genre:str = genre
    
    def set_director(self, director:str) -> None:
        if len(director) > 255:
            raise ValueError("Director name can't be longer than 255 characters!")
        self.director:str = director
    
    def set_writer(self, writer:str) -> None:
        if len(writer) > 255:
            raise ValueError("Writer name can't be longer than 255 characters!")
        self.writer:str = writer
    
    def set_actors(self, actors:str) -> None:
        self.actors:str = actors
    
    def set_plot(self, plot:str) -> None:
        self.plot:str = plot

    def set_score(self, score):
        if score != None and score < 0:
            raise ValueError("Score cannot be negative!")
        self.score:float = score
    
    def as_tuple(self) -> tuple[int, str, int, str, str, str, str, str, str, str, str, int]:
        return (self.imdbid, self.title, self.year, self.rating, self.runtime, self.genre, self.director, self.writer, self.actors, self.plot, self.score)
    
    def as_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "runtime": self.runtime,
            "rating": self.rating,
            "genre": self.genre,
            "director": self.director,
            "writer": self.writer,
            "actors": self.actors,
            "plot": self.plot,
            "score": self.score
        }