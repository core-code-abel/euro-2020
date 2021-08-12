# Dockerfile for STREAMLIT

FROM python:3.9.4

WORKDIR /front

ADD . .

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "/front/main.py"]