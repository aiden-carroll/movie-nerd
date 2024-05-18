from database import MovieDb
from models import Movie
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class App(ctk.CTk):
    def __init__(self, db, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db:MovieDb = db
        self.movies = self.db.search_title()
        self.title("Movie Nerd")
        self.geometry("800x400")

        self.bg_color = self._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
        self.text_color = self._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        self.selected_color = self._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        # Main Frame
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(side="left", fill="both", expand=True)

        # Search
        self.search_frame = ctk.CTkFrame(self.main_frame, height=20)
        self.search_frame.pack(fill="both", side="top")

        self.search_title_str = ctk.StringVar()
        self.search_title_str.trace_add("write", lambda name, index, mode: self.search_title())
        self.search_title_entry = ctk.CTkEntry(self.search_frame, textvariable=self.search_title_str)
        self.search_title_entry.pack(fill="x", expand=True)

        # Movie Table
        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure(
            "Treeview", 
            background="#2a2d2e", 
            foreground="white", 
            fieldbackground="#343638", 
            bordercolor="#343638",
            borderwidth=0
        )
        treestyle.map('Treeview', background=[('selected', "#22559b")])
        self.bind("<<TreeviewSelect>>", lambda event: self.focus_set())
        treestyle.configure(
            "Treeview.Heading",
            background="#565b5e",
            foreground="white",
            relief="flat"
        )
        treestyle.map("Treeview.Heading", background=[('active', "#3484F0")])

        self.table = ttk.Treeview(
            self.main_frame, 
            columns=["score", "title", "year"],
            show="headings"
        )
        self.table.column("score", minwidth=1, stretch=0, anchor="center")
        self.table.heading("score", text="Score")
        self.table.column("title")
        self.table.heading("title", text="Title")
        self.table.column("year", minwidth=1, stretch=0)
        self.table.heading("year", text="Year")

        self.table.pack(fill="both", expand=True)
        self.populate_table()

        # Movie Inspector
        self.inspect_frame = ctk.CTkFrame(self, width=20)
        self.inspect_title = ctk.CTkLabel(self.inspect_frame, text="undefined")
        self.inspect_title.pack()

    def search_title(self):
        self.movies = self.db.search_title(self.search_title_str.get())
        self.populate_table()
    
    def populate_table(self):
        self.clear_table()
        i = 0
        self.score_strings:list[ctk.StringVar] = []
        for m in self.movies:
            self.table.insert(
                parent="", 
                index=i, 
                values=(m.score, m.title, m.year)
            )
            i += 1
    
    def clear_table(self) -> None:
        for i in self.table.get_children():
            self.table.delete(i)
    
    def show_inspector(self) -> None:
        self.inspect_frame.pack(side="right", fill="both", expand=True)

    def hide_inspector(self) -> None:
        self.inspect_frame.forget()
    
    def inspect(self, movie:Movie) -> None:
        self.inspect_title._text = movie.title + "(" + str(movie.year) + ")"
        self.inspect_title.pack()
        self.show_inspector()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")