import json

import httpx
from pydantic import BaseModel
from httpx import Client
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema

class AuthenticationUserSchema(BaseModel): #Структура данных пользователя для авторизации
    email: str
    password: str

#Создаем private builder
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создает экземпляр httpx.Client с аутентификацией пользователя
    :param user: объект AuthenticationUserSchema c email и паролем пользователя
    :return: готовый к использованию httpx.Client с установленным заголовком Authorization
    """
    #Инициализируем AuthenticationClient для аутентификации
    authentication_client = get_authentication_client()

    #Инициализируем запрос на аутентификацию
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    #Выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        #Добавляем заголовок авторизации
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )
