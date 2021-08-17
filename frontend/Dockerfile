# Dockerfile for STREAMLIT

FROM python:3.9.4

WORKDIR /front

ADD . .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "/front/main.py"]