# Задание 7. FastAPI endpoint возвращает JSON
# Запуск: uvicorn task7_fastapi_json:app --reload
from fastapi import FastAPI

app = FastAPI()


@app.get("/info")
def info():
    return {"student": "Филатов Иван", "lab": 6, "variant": 2}
