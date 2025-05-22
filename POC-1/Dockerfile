FROM python:3.11

ENV DATABASE_URL="sqlite:///./todo.db"

WORKDIR /home/POC-1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./todo_app ./todo_app

WORKDIR /home/POC-1/todo_app

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000","--reload"]