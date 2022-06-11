import requests
import json

url = 'http://127.0.0.1:8090/ocr'
files = {'file': open('./demo.jpg', 'rb')} 
r = requests.post(url, files=files)
print(r.text)