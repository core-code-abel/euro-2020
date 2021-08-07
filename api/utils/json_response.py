from flask import Response
import json

def process_col(col):
    return col.split('.')[-1].split(' AS ')[-1]

def json_response(data, cols, status=200):
    print (data)
    return json.dumps([[{process_col(col): row[i]} for i, col in enumerate(cols)] for row in data])
