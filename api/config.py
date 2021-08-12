import os
import dotenv
import sys

dotenv.load_dotenv()

db_url = os.getenv('DATABASE_URL', 'postgresql+psycopg2://login:password@localhost:5432')