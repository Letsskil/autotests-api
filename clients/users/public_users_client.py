from clients.api_client import APIClient
from httpx import Response
from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema
from clients.publick_http_builder import get_public_http_client

class PublicUsersClient(APIClient):
    """
    Клиент для создания пользователя POST
/api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод выполняет создание пользователя
        :param request: словарь с данным которые необходимо отправить
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    # Добавляем новый метод получения JSON внутри клиента
    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

# Добавляем билдер для PublicUsersClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создает экземпляр PublicUsersClient с уже настроенным HTTP-клиентом
    :return: Готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())
