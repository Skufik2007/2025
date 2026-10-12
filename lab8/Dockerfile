# Повышенное задание 6. Docker для приложения
FROM python:3.12-slim

WORKDIR /app
RUN pip install requests pytest
COPY calc.py test_calc.py main.py ./

RUN pytest
CMD ["python", "main.py"]
