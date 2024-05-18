
from database import MovieDb
from gui import App
from api import *

db = MovieDb("data/movies.db")

for i in []:
    db.add(get_movie_from_id(i))

app = App(db)
app.mainloop()

db.close()