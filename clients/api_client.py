from typing import Any

from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles


class APIClient:
    def __init__(self, client: Client):
        """
        Базовый API клиент, принимающий объект httpx.Client.
        :param client: экземпляр httpx.Client для выполнения HTTP-запросов
        """
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Выполняет GET запрос.
        :param url: URL-адрес эндпоинта.
        :param params: GET-параметры запроса (например ?key=value).
        :return: Объект Response с данными ответа
        """
        return self.client.get(url, params=params)

    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """
        Выполняет POST запрос.

        :param url: адрес эндпоинта
        :param json: данные в фромате JSON
        :param data: форматированные данные формы (например, application/x-www-form-urlencoded).
        :param files: файлы для загрузки на сервер
        :return: данные ответа от сервера
        """
        return self.client.post(url, data=data, files=files, json=json)

    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Выполняет частичное обновление данных
        :param url: адрес эндпоинта
        :param json: данные для обновления в соответствующем формате
        :return: данные ответа от сервера
        """
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str) -> Response:
        """
        Выполняет удаление данных
        :param url: адрес эндпоинта
        :return: данные ответа от сервера
        """
        return self.client.delete(url)