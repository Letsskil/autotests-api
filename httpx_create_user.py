import httpx
from tools.fakers import fake

payload = {
    "email": fake.email(),
    "password": "1234",
    "lastName": "Igor",
    "firstName": "Igor",
    "middleName": "string"
}

response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())
