FROM python:3.9-slim

WORKDIR /app

COPY . /app

COPY Scores.txt /Scores.txt

COPY requirements.txt* /app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8777

CMD ["python", "main_score.py"]