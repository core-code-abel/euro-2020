from sqlalchemy import create_engine
from config import db_url


engine = create_engine(db_url)
connection = engine.connect()

def execute_query(query):
  return list(connection.execute(query))