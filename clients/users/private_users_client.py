from clients.api_client import APIClient
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema
from httpx import Response
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema

class PrivateUserClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")
    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по идентификатору
        :param user_id: Идентификатор пользователя
        :return: ответ от сервера
        """
        return self.get(f"/api/v1/users/{user_id}")
    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод обновления данных пользователя
        :param user_id: идентификатор пользователя
        :param request: словарь с данными которые необходимо отправить
        :return: ответ от сервера
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))
    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по его айди
        :param user_id: идентификатор пользователя
        :return: ответ от сервера
        """
        return self.delete(f"/api/v1/users/{user_id}")

    # Добавляем новый метод получения JSON внутри клиента
    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

#Добавляем билдер для PrivateUserClient
def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUserClient:
    """
    Функция создает экзмепляр PrivateUserClient с уже настроенным HTTP-клиентом
    :param user:
    :return: готовый к использованию PrivateUserClient
    """
    return PrivateUserClient(client=get_private_http_client(user))
    
