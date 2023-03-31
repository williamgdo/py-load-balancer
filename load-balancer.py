# basic server example

import requests
from flask import Flask

app = Flask(__name__)
# loadbalancer = Flask(__name__)

BACKENDS = ['http://power1:5000', 'http://power2:5000']
# 5000 is the default port for flask applications 

  
@app.route('/power', methods=['POST'])
def toDistribute():
  x = 2
  y = 4
  dictToSend = { x, y }
  
  try:
    res = requests.post('http://service/calculate', json=dictToSend)

    print ('response from server:',res.text)
    dictFromServer = res.json()
  except:
    print("An exception occurred") 

if __name__ == '__main__':
  app.run(host='0.0.0.0')
