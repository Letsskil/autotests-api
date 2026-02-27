import httpx

#Проходим аутентификацию
login_payload = {
    # "email": "user@example.com",
    "email": "test.1769515942.6072607@example.com",
    # "password": "string"
    "password": "Qwerty876"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

#Инициализируем клиент с base_url
client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=10, #Таймаут в секундах
    headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
)

#Выполняем GET-запрос, используя клиент
get_user_me_response = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me_response.json()
print('Get user me data:', get_user_me_response_data)

