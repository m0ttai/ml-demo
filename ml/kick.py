import requests
import json

url = 'http://127.0.0.1/'
payload = {"file_name": "cat.jpg"}

res = requests.post(url, json=json.dumps(payload))

print(res.headers)
print(res.text)