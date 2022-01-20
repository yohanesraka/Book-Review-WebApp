import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask

app = Flask(__name__)

engine = create_engine(os.getenv(uri))
db = scoped_session(sessionmaker(bind=engine))


def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",{"isbn": isbn, "title": title, "author": author, "year": year})
        db.commit()
        print(f"Inserted into the DATABASE : ISBN : {isbn} , Title : {title} , Author : {author}, Year : {year}.")

main()
