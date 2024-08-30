import requests
from configuration.ConfigProvider import ConfigProvider
import requests
import allure

from pathlib import Path

# Задаём корневой путь проекта.
root_path = Path(__file__).resolve().parents[1]
print(root_path)

class ApiReadCity:
    """
    Класс для работы с API чтения города.
    Атрибуты:
        base_url (str): Базовый URL API.
        city_id (int): Идентификатор города.
        token (str): Токен авторизации.

    Методы:
        get_headers() -> dict: Возвращает заголовки для запросов.
        get(endpoint: str, params: dict) -> requests.Response: Выполняет GET запрос.
        search_product(phrase: str, page: int, per_page: int, sort: str) -> requests.Response: Выполняет поиск товара.
        post(endpoint: str, data: dict) -> requests.Response: Выполняет POST запрос.
        add_bookmark(book_id: int) -> requests.Response: Добавляет книгу в закладки.
        delete(endpoint: str, data: dict) -> requests.Response: Выполняет DELETE запрос.
        remove_bookmark(book_id: int) -> requests.Response: Удаляет книгу из закладок.
        patch(endpoint: str, data: dict) -> requests.Response: Выполняет PATCH запрос.
        update_personal_data(personal_data: dict) -> requests.Response: Обновляет персональные данные.
    """
    def __init__(self, config_provider: ConfigProvider):
        api_config = config_provider.get_api_config()
        self.base_url = api_config['base_url']
        self.city_id = api_config['city_id']
        self.token = api_config['token']

    @allure.step("Получить заголовки для запроса")
    def get_headers(self):
        headers = {}
        if self.token:
            headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
            }
        return headers
    
    @allure.step("Выполнить GET запрос")
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        headers = self.get_headers()
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response

    @allure.step("Выполнить поиск товара")
    def search_product(self, phrase, page=1, per_page=10, sort="relevance"):
        endpoint = "/v2/search/product"
        params = {
            'customerCityId': self.city_id,
            'phrase': phrase,
            'products[page]': page,
            'products[per-page]': per_page,
            'sortPreset': sort
        }
        return self.get(endpoint, params=params)

    @allure.step("Выполнить POST запрос")
    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        headers = self.get_headers()
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response

    @allure.step("Добавить книгу в закладки")
    def add_bookmark(self, book_id):
        endpoint = "/v1/bookmarks"
        data = {"id": book_id}
        response = self.post(endpoint, data=data)
        return response

    @allure.story("Выполнить DELETE запрос")
    def delete(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        headers = self.get_headers()
        response = requests.delete(url, json=data, headers=headers)
        response.raise_for_status()
        return response
    
    @allure.step("Удалить книгу из закладок")
    def remove_bookmark(self, book_id):
        endpoint = "/v1/bookmarks/3026125"
        data = {"id": book_id}
        return self.delete(endpoint, data=data)
    
    @allure.step("Выполнить PATCH запрос")
    def patch(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        headers = self.get_headers()
        response = requests.patch(url, json=data, headers=headers)
        response.raise_for_status()
        return response

    @allure.step("Обновить персональные данные пользователя")
    def update_personal_data(self, personal_data):
        endpoint = "/v1/profile/personal-data"
        return self.patch(endpoint, data=personal_data)