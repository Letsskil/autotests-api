import uuid
from pydantic import BaseModel, ConfigDict, Field, EmailStr, HttpUrl, ValidationError
from pydantic.alias_generators import to_camel

# class CourseSchema(BaseModel):
#     # Автоматическое преобразование snake_case -> camelCase
#     model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
#
#     id: str
#     title: str
#     max_score: int
#     min_score: int
#     description: str
#     estimated_time: str

# Инициализация модели CourseSchema через передачу аргументов
# course_default_model = CourseSchema(
#     id="course-id",
#     title="Playwright",
#     maxScore=100,
#     minScore=10,
#     description="Playwright",
#     estimatedTime="1 week"
# )
# print('Course default model:', course_default_model)

# Инициализация модели CourseSchema через распаковку словаря
# course_dict = {
#     "id": "course-id",
#     "title": "Playwright",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "Playwright",
#     "estimatedTime": "1 week"
# }
# course_dict_model = CourseSchema(**course_dict)
# print('Course dict model:', course_dict_model.model_dump_json(by_alias=True))

# Инициализация модели CourseSchema через JSON
# course_json = """
# {
#     "id": "course-id",
#     "title": "Playwright",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "Playwright",
#     "estimatedTime": "1 week"
# }
# """
# course_json_model = CourseSchema.model_validate_json(course_json)
# print('Course JSON model:', course_json_model.model_dump_json(by_alias=True))


# Добавили модель FileSchema
class FileSchema(BaseModel):
    id: str
    url: HttpUrl # Используем HttpUrl вместо str
    filename: str
    directory: str

#Добавили модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    # Добавим метод формирования имени пользователя
    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"
    """
Использование методов в Pydantic-модели – хотя Pydantic в основном используется для валидации и сериализации данных, мы можем добавлять методы для удобного представления или обработки данных.
Метод get_username – возвращает строку с полным именем пользователя, объединяя first_name и last_name.
Использование аннотации типов – метод возвращает str, что делает код более читаемым.
    """

# Значения по умолчанию + вычисляемое значение по умолчанию для динамических элементов
class CourseSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    # Вложенный объект для файла-превью
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    #Вложенный объект для пользователя, создавшего курс
    created_by_user: UserSchema = Field(alias="createdByUser")

"""
В Pydantic можно использовать вложенные модели, чтобы структурировать сложные JSON-данные.
3 вида Инициализации: передача аргументов, dict (распаковка словаря), JSON.
Pydantic автоматически преобразует вложенные структуры в соответствующие модели, если данные корректно переданы.
Использование Field(alias="…") позволяет задавать соответствие между Python-атрибутами и JSON-ключами.
"""
# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    # Добавили инициализацию вложенной модели FileSchema
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses",
    ),
    estimatedTime="1 week",
    # Добавили инициализацию вложенной модели UserSchema
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alise"
    )
)
print('Course default model:', course_default_model)

# Инициализируем модель CourseSchema через распаковку словаря
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    # Добавили ключ previewFile
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    # Добавили ключ createdByUser
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)
print(course_dict_model.model_dump())
print(course_dict_model.model_dump(by_alias=True))

# Инициализируем модель CourseSchema через JSON
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)

# Обработки ошибки с некорректным url
try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses",
    )
except ValidationError as error:
    print(error)
    print(error.errors())
"""
error содержит текст ошибки с пояснением.
error.errors() возвращает список словарей с подробной информацией об ошибке, например:
[
    {
        'loc': ('url',),
        'msg': 'Input should be a valid URL, relative URL without a base',
        'type': 'url_parsing',
        'input': 'localhost',
    }
]
"""