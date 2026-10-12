# Лабораторная работа 1. Система контроля версий Git

## Задания средней сложности

1. Установка и настройка Git:
```
git --version
git config --global user.name "Ivan Filatov"
git config --global user.email "ivanfilatov321@gmail.com"
```
2. Создание репозитория: `git init`
3. Первый коммит: `git add main.py` и `git commit -m "ЛР 1: первый коммит"`
4. Изменил main.py, второй коммит: `git commit -am "ЛР 1: второй коммит"`
5. Ветка feature: `git checkout -b feature`, добавил feature.py, закоммитил
6. Слияние: `git checkout main` и `git merge feature`
7. Создал .gitignore (`__pycache__/`, `*.pyc`, `.env`)
8. Связь с GitHub: `git remote add origin https://github.com/ideal1351/2025.git`
9. Отправка: `git push -u origin main`
10. Клонирование чужого репозитория и просмотр истории:
```
git clone https://github.com/Skufik2007/my-python-project.git
git log --oneline
```

## Повышенной сложности

**2. SSH-ключ**
```
ssh-keygen -t ed25519 -C "ivanfilatov321@gmail.com"
cat ~/.ssh/id_ed25519.pub
```
Скопировал ключ в GitHub → Settings → SSH and GPG keys → New SSH key.
Проверка: `ssh -T git@github.com`

**6. GitHub Actions**

Файл `.github/workflows/python-check.yml` — при каждом push проверяет код
через flake8 и запускает тесты pytest (вкладка Actions на GitHub).
