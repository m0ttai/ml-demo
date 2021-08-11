import requests
import json

# url = 'http://127.0.0.1'
url = 'http://35.187.223.154:10080/'
payload = {"file_name": "cat.jpg"}

res = requests.post(url, json=json.dumps(payload))

print(res.headers)
print(res.text)