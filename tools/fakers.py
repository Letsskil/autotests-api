from faker import Faker

class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker
    """
    def __init__(self, faker:Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных
        """
        self.faker = faker

    def text(self) -> str:
        """
        Генерирует случайный текст
        :return: Случайный текст
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Генерирует случайный UUID4
        :return: Случайный UUID4
        """
        return self.faker.uuid4()

    def email(self) -> str:
        """
        Генерирует случайный email
        :return: случайный email
        """
        return self.faker.email()

    def sentence(self) -> str:
        """
        Генерирует случайное предложение
        :return: случайное предложение
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерирует случайный пароль
        :return: случайный пароль
        """
        self.faker.password()

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию
        :return: случайную фамилию
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Генерирует случайное имя
        :return: случайное имя
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество/среднее имя
        :return:случайное отчество/среднее имя
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Генерирует строку с предполагаемым временем (например, "2 weeks")
        :return: строка с предполагаемым временем
        """
        return f"{self.integer(1, 10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерирует случайное число в заданном диапазаоне
        :param start: начало диапазаона (включительно)
        :param end: конец диапазона (включительно)
        :return: случайное целое число
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        Генерирует случайный максимальный бал в диапазоне от 50 до 100
        :return: случайный бал
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Генерирует случайный минимальный бал в диапазаоне от 1 до 30
        :return: случайный бал
        """
        return self.integer(1, 30)

fake = Fake(faker=Faker())

