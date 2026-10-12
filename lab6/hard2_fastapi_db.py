# Повышенное задание 2. FastAPI с базой данных (SQLite)
# Запуск: uvicorn hard2_fastapi_db:app --reload, документация: /docs
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

conn = sqlite3.connect("notes.db", check_same_thread=False)
conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)")
conn.commit()


class Note(BaseModel):
    text: str


@app.get("/notes")
def get_notes():
    rows = conn.execute("SELECT id, text FROM notes").fetchall()
    return [{"id": r[0], "text": r[1]} for r in rows]


@app.post("/notes")
def add_note(note: Note):
    cur = conn.execute("INSERT INTO notes (text) VALUES (?)", (note.text,))
    conn.commit()
    return {"id": cur.lastrowid, "text": note.text}


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    cur = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    return {"deleted": note_id}
