from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    CreateExerciseResponseSchema, UpdateExercisesRequestSchema, GetExercisesResponseSchema, \
    UpdateExerciseResponseSchema, GetExerciseResponseSchema


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий
        :param query: словарь с courseID
        :return: ответ от сервера
        """
        return self.get(f"/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения конкретного задания по его идентификатору
        :param exercise_id: идентификатор задания
        :return: ответ от сервера
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercises_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания
        :param request: словарь с данным которые нужно отправить
        :return: ответ от сервера
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercises_api(self, exercise_id: str, request: UpdateExercisesRequestSchema) -> Response:
        """
        Метод обновления задания
        :param exercise_id: идентификатор задания
        :param request: словарь с данным которые нужно отправить
        :return: ответ от сервера
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercises_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления задания
        :param exercise_id: идентификатор задания
        :return: ответ от сервера
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    # Добавляем новый метод получения списка заданий
    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    # Добавляем новый метод получения задания
    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    # Добавляем новый метод создания задания
    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercises_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    # Добавляем новый метод обновления задания
    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.create_exercises_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

#Добавляем билдер для ExercisesClient
def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создает экземпляр ExercisesClient с уже настроенным HTTP-клиентом
    :param user:
    :return: готовый к использованию ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))
