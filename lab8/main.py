# Задания 2 и 7. Использование requests (добавлен через poetry) и logging
import logging

import requests

from calc import add, div

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("app.log", encoding="utf-8"), logging.StreamHandler()],
)

logging.info("Программа запущена")
logging.info("2 + 3 = %s", add(2, 3))

try:
    div(1, 0)
except ValueError:
    logging.warning("Поймали деление на ноль")

try:
    response = requests.get("https://api.github.com", timeout=5)
    logging.info("Ответ GitHub API: код %s", response.status_code)
except requests.RequestException as error:
    logging.error("Нет соединения: %s", error)

logging.info("Программа завершена")
