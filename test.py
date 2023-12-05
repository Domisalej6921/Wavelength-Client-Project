import requests

r = requests.session()

json = {
    "email": "dom69@gmail.com",
    "password": "Password1"
}

r.post('http://127.0.0.1:5000/auth/login', json=json)

json = {
    "limit": 12
}

data = r.post('http://127.0.0.1:5000/api/mentors', json=json)

print(data.text)