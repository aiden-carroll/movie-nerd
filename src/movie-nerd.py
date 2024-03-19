
from database import MovieDb
from gui import App

db = MovieDb("data/movies.db")

app = App(db)
app.mainloop()

db.close()