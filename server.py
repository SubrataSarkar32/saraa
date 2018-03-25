from flask import Flask, request, jsonify
import json
import requests
import os
import os

os.environ.setdefault('REQUEST_TOKEN', '41befe6e62cef612efc7eee3c1cebefc')
os.environ.setdefault('LANGUAGE', 'en')
app = Flask(__name__)
port = int(os.environ["PORT"])
print(port)

@app.route('/', methods=['POST'])
def index(): 
  print(json.loads(request.get_data())) 
  return jsonify( 
    status=200, 
    replies=[{ 
      'type': 'text', 
      'content': 'Roger that', 
    }], 
    conversation={ 
      'memory': { 'key': 'value' } 
    } 
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port, host="0.0.0.0")
