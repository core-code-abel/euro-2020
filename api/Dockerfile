FROM python:3.9.4

WORKDIR /api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python","/api/server.py"]
