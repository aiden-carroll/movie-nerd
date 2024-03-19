from database import MovieDb
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class App(ctk.CTk):
    def __init__(self, db, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db:MovieDb = db
        self.title("Movie Nerd")
        self.geometry("400x400")

        # Movie Table
        self.table = ttk.Treeview(
            self,
            columns=("title", "year"),
            show="headings",
        )
        self.table.heading("title", text="Title")
        self.table.heading("year", text="Year")
        self.table.pack()
        self.populate_table()
    
    def populate_table(self):
        movies = self.db.get_alphabetical()
        i = 0
        for m in movies:
            self.table.insert(parent="", index=i, values=(m.title, m.year))
            i += 1
        

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")