import requests

headers = {}

r = requests.get('http://127.0.0.1:8000/hi', headers=headers)

print(r.json())
