from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCourseResponseSchema, CreateCoursesRequestSchema, UpdateCoursesRequestSchema

class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов
        :param query: словарь с userID
        :return: ответ от сервера
        """
        return self.get(f"/api/v1/courses", params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения конкретного курса по его идентификатору
        :param course_id: идентификатор курса
        :return: ответ от сервера
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_courses_api(self, request: CreateCoursesRequestSchema) -> Response:
        """
        Метод создания курса
        :param request: словарь с данным которые нужно отправить
        :return: ответ от сервера
        """
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))

    def update_courses_api(self, course_id: str, request: UpdateCoursesRequestSchema) -> Response:
        """
        Метод обновления курса
        :param course_id: идентификатор курса
        :param request: словарь с данным которые нужно отправить
        :return: ответ от сервера
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    def delete_courses_api(self, course_id: str) -> Response:
        """
        Метод для удаления курса
        :param course_id: идентификатор курса
        :return: ответ от сервера
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    # Добавляем новый метод создания курса
    def create_course(self, request: CreateCoursesRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_courses_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

#Добавляем билдер для CoursesClient
def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Функция создает экземпляр CoursesClient с уже настроенным HTTP-клиентом
    :param user:
    :return: готовый к использованию CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user))
