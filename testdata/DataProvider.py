import json
import allure

"""Загружаем глобальные данные из файла 'test_data.json'."""
my_file = open('test_data.json')
global_data = json.load(my_file)

class DataProvider:
    """
    Класс для предоставления тестовых данных.
    Атрибуты:
        data (dict): Тестовые данные из JSON файла.
    Методы:
        get_search_tests() -> list: Возвращает тесты для поиска.
        get_personal_data_tests() -> list: Возвращает тесты для персональных данных.
        get_search_data() -> dict: Возвращает данные для поиска.
        get_book_id() -> int: Возвращает ID книги.
    """
    
    def __init__(self) -> None:
        self.data = global_data

    @allure.step("Получить данные для поиска из файла test_data.json")
    def get_search_tests(self):
        return self.data.get('search_tests', [])

    @allure.step("Получить тесты для персональных данных")
    def get_personal_data_tests(self):
        return [self.data.get('personal_data', {})]
    
    @allure.step("Получить данные для поиска")
    def get_search_data(self):
        return self.data['search_data']
    
    @allure.step("Получить ID книги")
    def get_book_id(self):
        return self.data['book_id']