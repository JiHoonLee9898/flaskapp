from flask import Flask
from flask import request

import requests
import re
import socket

app = Flask(__name__)

# 컴퓨터 이름, ip
hostname = socket.gethostname()
hostip = socket.gethostbyname(socket.gethostname())

#외부 IP, 아래 사이트 호출 후 결과에서 추출
req = requests.get("http://ipconfig.kr")
out_ip = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

@app.route('/')
def hello_world():
    return 'Hello, Flask!'
