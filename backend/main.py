from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool


def get_connection():
    connection = sqlite3.connect("todos.db")
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
        """
    )

    cursor = connection.execute("SELECT COUNT(*) FROM todos")
    count = cursor.fetchone()[0]

    if count == 0:
        connection.executemany(
            """
            INSERT INTO todos (title, description, completed)
            VALUES (?, ?, ?)
            """,
            [
                (
                    "Complete assessment",
                    "Finish the Todo List application assessment.",
                    0,
                ),
                (
                    "Study HTML",
                    "Review HTML structure and elements.",
                    1,
                ),
                (
                    "Practice JavaScript",
                    "Practice JavaScript concepts and DOM manipulation.",
                    0,
                ),
                (
                    "Build the backend",
                    "Create the FastAPI backend for the Todo List.",
                    0,
                ),
                (
                    "Test the application",
                    "Test the completed Todo List application.",
                    1,
                ),
            ],
        )

    connection.commit()
    connection.close()


initialize_database()


@app.get("/")
def home():
    return {"message": "Todo API is running"
    ""}
@app.get("/todos")
def get_todos():
    connection = get_connection()

    cursor = connection.execute("SELECT * FROM todos")
    rows = cursor.fetchall()

    connection.close()

    todos_list = [Todo(**dict(row)) for row in rows]

    return todos_list