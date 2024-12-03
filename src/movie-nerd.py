
from database import MovieDb
from gui import App
from api import API

db = MovieDb.get_instance("data/movies.db")

for i in ["tt4034228"]:
    movie = API.get_movie_from_id(i)
    print(movie.title)
    db.add(movie)

#app = App(db)
#app.mainloop()

db.close()