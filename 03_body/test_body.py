import requests

r = requests.post('http://127.0.0.1:8000/hi', json={'who': 'Mom'})

print(r.json())
