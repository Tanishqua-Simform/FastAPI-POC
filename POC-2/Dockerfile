FROM python:3.11

WORKDIR /home/POC-2

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./auth_app ./auth_app

WORKDIR /home/POC-2/auth_app

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000","--reload"]