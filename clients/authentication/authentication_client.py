from clients.api_client import APIClient
from httpx import Response
from clients.publick_http_builder import get_public_http_client #Импортируем билдер
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema, RefreshRequestSchema


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.
        :param request: Словарь с email и password
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/authentication/login",
            json=request.model_dump(by_alias=True)
        )

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации
        :param request: Словарь с рефреш токеном
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/authentication/refresh",
            json=request.model_dump(by_alias=True)
        )

    #Добавили метод Login
    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request) #Отправляем запрос на аутентификацию
        if response.status_code != 200:
            print(f"Auth failed: {response.status_code}")
            print(f"Response text: {response.text}")
            response.raise_for_status()

        return LoginResponseSchema.model_validate_json(response.text)

# Добавляем билдер для AuthenticationClient
def get_authentication_client() -> AuthenticationClient:
    """
    Функция создает готовый экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию AuthenticationClient
    """
    return AuthenticationClient(client=get_public_http_client())
