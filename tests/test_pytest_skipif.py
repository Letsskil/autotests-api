import pytest

SYSTEM_VERSION = "v1.2.0" # Для примера укажем версию тестируемой системы

@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0", # Пропускаем автотест, если версия системы равна v1.3.0
    reason="Тест не может быть запущен на версии системы v1.3.0"
)
def test_system_version_valid(): # В текущей конфигурации этот запустится
    pass

@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.0",  # Пропускаем автотест, если версия системы равна v1.2.0
    reason="Тест не может быть запущен на версии системы v1.2.0"
)
def test_system_version_invalid(): # Этот автотест запустится
    pass
