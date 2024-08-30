import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from configuration.ConfigProvider import ConfigProvider

class HomePage:
    """
    Класс для взаимодействия с главной страницей сайта.
    Атрибуты:
        __url (str): URL главной страницы.
        __driver (WebDriver): Объект веб-драйвера.
    Методы:
        go(): Открывает главную страницу.
        search(query: str): Выполняет поиск по введенному запросу.
        click_search_button(): Нажимает кнопку поиска.
        get_search_result_message() -> str: Получает сообщение о результате поиска.
    """
    def __init__(self, driver, config_provider: ConfigProvider):
        ui_config = config_provider.get_ui_config()
        self.__url = ui_config['homepage_url']
        self.__driver = driver

    @allure.step("Получение главной страницы")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Ввести данные в поисковую строку")
    def search(self, query):
        self.__driver.find_element(By.CSS_SELECTOR, 'input[enterkeyhint="search"]').send_keys(query)
    
    @allure.step("Нажать на кнопку поиска")
    def click_search_button(self):
        self.__driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Искать"]').click()
    
    @allure.step("Получить страницу с результатом поиска")
    def get_search_result_message(self) -> str:
        try:
            result_element_1 = WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.search-page__found-message')))
            result_element_1 = self.__driver.find_element(By.CSS_SELECTOR, "p.search-page__found-message")
            result_text = result_element_1.text
            return result_text
        except TimeoutException:
            try:
                result_element_2 = WebDriverWait(self.__driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h4.catalog-empty-result__header')))
                result_element_2 = self.__driver.find_element(By.CSS_SELECTOR, "h4.catalog-empty-result__header")
                return result_element_2.text
            except TimeoutException:
                return "Результаты поиска не найдены, и элемент для отображения пустого результата отсутствует."