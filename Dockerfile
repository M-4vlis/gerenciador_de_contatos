FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN mkdir -p data && touch data/contatos.json

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "scripts/main.py"]