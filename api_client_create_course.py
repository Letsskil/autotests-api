from clients.courses.courses_client import get_courses_client, CreateCoursesRequestSchema
from clients.files.files_client import get_files_client, CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_user_client, CreateUserRequestSchema

public_users_client = get_public_user_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema(password="test123")
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# Инициализируем клиенты
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestSchema(
    upload_file = "./testdata/files/Блок-схемы.png"
)
# print(create_file_request)

create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCoursesRequestSchema(
    preview_file_id = create_file_response.file.id,  # Передаем аргументы в формате snake_case вместо camelCase
    created_by_user_id = create_user_response.user.id  # Передаем аргументы в формате snake_case вместо camelCase
)
created_course_response = courses_client.create_course(create_course_request)
print('Create course data:', created_course_response)

