# Лабораторная работа 8. Экосистема Python — вариант 2

| Задание | Что сделано |
|---|---|
| Средн. 2 — добавить зависимость requests | `poetry init`, `poetry add requests` → pyproject.toml и poetry.lock; requests используется в main.py |
| Средн. 4 — TDD для калькулятора | сначала написан test_calc.py, потом calc.py |
| Средн. 7 — использовать logging | main.py пишет лог в консоль и в файл app.log |
| Повыш. 2 — CI GitHub Actions (pytest) | `.github/workflows/python-check.yml` в корне репозитория |
| Повыш. 6 — Docker для приложения | Dockerfile |

## Команды

```
pip install poetry
poetry install
poetry run pytest
poetry run python main.py

docker build -t lab8 .
docker run lab8
```
