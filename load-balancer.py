# basic server example

import requests
from flask import Flask

app = Flask(__name__)
# loadbalancer = Flask(__name__)

BACKENDS = ['http://power1:5000', 'http://power2:5000']
# 5000 is the default port for flask applications 

@app.route('/')
def sample():
  response = requests.get('http://service:5000/')
  return response.content, response.status_code

  # return f'This is the load balancer application.'
  
@app.route('/power', methods=['POST'])
def toDistribute():
  return f'This is the load balancer application.'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
