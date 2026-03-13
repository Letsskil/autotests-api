from http import HTTPStatus
from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from tests.conftest import UserFixture
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema
import pytest

@pytest.mark.regression
@pytest.mark.authentication
def test_login(function_user: UserFixture, authentication_client: AuthenticationClient):

    # Запрос на логин (login_request -> request)
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    # Выполняем логин (login_response -> response)
    response = authentication_client.login_api(request)
    # Валидация ответа (login_response_data -> response_data)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    # # Формируем тело запроса на создание пользователя
    # create_user_request = CreateUserRequestSchema(password="QWE123q")
    # # Отправляем запрос на создание пользователя
    # public_users_client.create_user(create_user_request)

    # # Выполняем аутентификацию
    # login_request = LoginRequestSchema(
    #     email=create_user_request.email,
    #     password=create_user_request.password
    # )
    # login_response = authentication_client.login_api(login_request)
    # login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    # Проверяем статус-код ответа
    assert_status_code(response.status_code, HTTPStatus.OK)
    # Проверяем корректность тела ответа
    assert_login_response(response_data)
    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())

