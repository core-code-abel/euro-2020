# Dockerfile for STREAMLIT

FROM python:3.9.4

ADD . .

RUN pip install -r requirements.txt

CMD streamlit run main.py --server.port $PORT