# 1.	Создайте базу данных library.db, содержащую 3 таблицы:
import sqlite3
connection = sqlite3.connect('library.db')
cursor = connection.cursor()
data_books = cursor.execute('''
create table if not exists books
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
author TEXT,
year INTEGER,
status TEXT CHECK (status = 'available' or status = 'borrowed')
) 
''')
data_readers = cursor.execute('''
CREATE TABLE IF NOT EXISTS readers 
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER
)
''')

data_borrowed_books = cursor.execute('''
CREATE TABLE IF NOT EXISTS borrowed_books
(
reader_id INTEGER,
book_id INTEGER,
borrow_date TEXT,
FOREIGN KEY (reader_id) REFERENCES readers(id),
FOREIGN KEY (book_id) REFERENCES books(id)
)
''')

connection.commit()
connection.close()

# 2.	Используйте dataclass для представления книг и читателей.
from dataclasses import dataclass
@dataclass
class Book:
   id: int
   title: str
   author: str
   year: int
   status: str
@dataclass
class Reader:
   id: int
   name: str
   age: int

# 3.	Создать класс Library для работы с базой. Этот класс будет управлять книгами, читателями и выдачей книг.
# 3.	Создать класс Library для работы с базой. Этот класс будет управлять книгами, читателями и выдачей книг.
import sqlite3


class Library:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
        create table if not exists books
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        year INTEGER,
        status TEXT DEFAULT 'available' CHECK (status = 'available' or status = 'borrowed')
        ) 
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS readers 
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrowed_books
        (
        reader_id INTEGER,
        book_id INTEGER,
        borrow_date TEXT,
        FOREIGN KEY (reader_id) REFERENCES readers(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
        )
        ''')
        self.conn.commit()

    def add_book(self, title, author, year):
        self.cursor.execute('INSERT INTO books(title, author, year) VALUES (?, ?, ?)',
                            (title, author, year))
        self.conn.commit()
        print(f'книга {title} добалена ')

    def add_reader(self, name, age):
        self.cursor.execute('INSERT INTO readers (name, age) VALUES (?, ?)', (name, age))
        self.conn.commit()
        print(f'пользователь {name} добавлен ')

    def borrow_book(self, reader_id, book_id):
        self.cursor.execute('SELECT status FROM books WHERE id = ?', (book_id,))
        data = self.cursor.fetchone()
        if data[0] == 'available':
            self.cursor.execute('UPDATE books SET status = "borrowed" WHERE id = ?', (book_id,))
            self.cursor.execute('INSERT INTO borrowed_books(reader_id, book_id) VALUES (?, ?)',
                                (reader_id, book_id))
            self.conn.commit()
            print(f'книга {book_id} выдана {reader_id} ')
        else:
            print('книга недоступна')

    def return_book(self, book_id):
        self.cursor.execute('UPDATE books SET status = "available" WHERE id = ?', (book_id,))
        self.cursor.execute('DELETE FROM borrowed_books WHERE book_id =?', (book_id,))
        self.conn.commit()
        print(f'книга {book_id} возвращена ')

    def search_books(self, keyword):
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
                            (f"%{keyword}%", f"%{keyword}%"))
        data = self.cursor.fetchall()
        for item in data:
            print(item)

    def get_borrowed_books(self):
        self.cursor.execute('''SELECT readers.name, books.title FROM borrowed_books 
                            INNER JOIN readers ON readers.id = borrowed_books.reader_id
                            INNER JOIN books ON books.id = borrowed_books.book_id''')
        data = self.cursor.fetchall()
        for item in data:
            print(f"Читатель {item[0]} взял '{item[1]}'")

    def get_statistics(self):
        self.cursor.execute("SELECT status, COUNT(*) FROM books GROUP BY status")
        data = self.cursor.fetchall()
        for item in data:
            print(f"Статус '{item[0]}': {item[1]} шт.")
library = Library('library.db')
library.add_book(title = 'bbbb', author='aaaa', year=1111)
library.add_reader(name='biba',age=13)
library.borrow_book(reader_id=1,book_id=1)
library.return_book(book_id=1)
library.search_books(keyword='bbb')
library.get_borrowed_books()
library.get_statistics()


