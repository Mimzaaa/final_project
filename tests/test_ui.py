import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from configuration.ConfigProvider import ConfigProvider
from pages.ui_class import HomePage
from testdata.DataProvider import DataProvider

@allure.title("Проверка работы поля 'Поиск'")
def test_search_functionality_val_1(browser: WebDriver, config_provider: ConfigProvider, data_provider: DataProvider):
    home_page = HomePage(browser, config_provider)
    home_page.go()
    
    search_data = data_provider.get_search_data()
    home_page.search(search_data['ui_phrase_val_1'])
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert "Показываем результаты по запросу «проверка»" in result_message, "Текст не соответствует ожидаемому"

@allure.title("Поле 'Поиск' принимает данные на латинице")
def test_search_functionality_val_2(browser: WebDriver, config_provider: ConfigProvider, data_provider: DataProvider):
    home_page = HomePage(browser, config_provider)
    home_page.go()

    search_data = data_provider.get_search_data()
    home_page.search(search_data['ui_phrase_val_2'])
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert "Показываем результаты по запросу «the miracle morning»" in result_message, "Текст не соответствует ожидаемому"

@allure.title("Поле 'Поиск' принимает данные состоящие из 2 букв")
def test_search_functionality_val_3(browser: WebDriver, config_provider: ConfigProvider, data_provider: DataProvider):
    home_page = HomePage(browser, config_provider)
    home_page.go()

    search_data = data_provider.get_search_data()
    home_page.search(search_data['ui_phrase_val_3'])
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert "Показываем результаты по запросу «bl»" in result_message, "Текст не соответствует ожидаемому"

@allure.title("Поле 'Поиск' принимает данные с пропущенной буквой")
def test_search_functionality_val_4(browser: WebDriver, config_provider: ConfigProvider, data_provider: DataProvider):
    home_page = HomePage(browser, config_provider)
    home_page.go()

    search_data = data_provider.get_search_data()
    home_page.search(search_data['ui_phrase_val_4'])
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert "Показываем результаты по запросу «ревизор»" in result_message, "Текст не соответствует ожидаемому"

@allure.title("Поле 'Поиск' принимает данные с символом на конце запроса")
def test_search_functionality_val_5(browser: WebDriver, config_provider: ConfigProvider, data_provider: DataProvider):
    home_page = HomePage(browser, config_provider)
    home_page.go()

    search_data = data_provider.get_search_data()
    home_page.search(search_data['ui_phrase_val_5'])
    home_page.click_search_button()

    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert "Показываем результаты по запросу «ревизор»" in result_message, "Текст не соответствует ожидаемому"

@allure.title("Поле 'Поиск' не принимает данные, состоящие из двух слов без пробела")
def test_search_functionality_neg_1(browser: WebDriver, config_provider: ConfigProvider, data_provider: DataProvider):
    home_page = HomePage(browser, config_provider)
    home_page.go()

    search_data = data_provider.get_search_data()
    home_page.search(search_data['ui_phrase_neg_1'])
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert "Похоже, у нас такого нет" in result_message, "Текст не соответствует ожидаемому"

@allure.title("Поле 'Поиск' не принимает данные, состоящие из одной буквы")
def test_search_functionality_neg_2(browser: WebDriver, config_provider: ConfigProvider, data_provider: DataProvider):
    home_page = HomePage(browser, config_provider)
    home_page.go()

    search_data = data_provider.get_search_data()
    home_page.search(search_data['ui_phrase_neg_2'])
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()
    
    with allure.step("Результат: " + result_message):
        assert "Похоже, у нас такого нет" in result_message, "Текст не соответствует ожидаемому"

@allure.title("Поиск товара с помощью символов")
def test_search_functionality_neg_3(browser: WebDriver, config_provider: ConfigProvider, data_provider: DataProvider):
    home_page = HomePage(browser, config_provider)
    home_page.go()

    search_data = data_provider.get_search_data()
    home_page.search(search_data['ui_phrase_neg_3'])
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()
    
    with allure.step("Результат: " + result_message):
        assert "Похоже, у нас такого нет" in result_message, "Текст не соответствует ожидаемому"

@allure.title("Поиск товара с пустым полем")
def test_search_functionality_neg_4(browser:  WebDriver, config_provider: ConfigProvider, data_provider: DataProvider):
    home_page = HomePage(browser, config_provider)
    home_page.go()

    search_data = data_provider.get_search_data()
    home_page.search(search_data['ui_phrase_neg_4'])
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert result_message == "Результаты поиска не найдены, и элемент для отображения пустого результата отсутствует."

@allure.title("Поиск товара с данными из пробелов")
def test_search_functionality_neg_5(browser: WebDriver, config_provider: ConfigProvider, data_provider: DataProvider):
    home_page = HomePage(browser, config_provider)
    home_page.go()

    search_data = data_provider.get_search_data()
    assert search_data['ui_phrase_neg_5'] == ' ' * 5, "Данные для поиска не соответствуют ожиданиям"

    search_data = data_provider.get_search_data()
    home_page.search(search_data['ui_phrase_neg_5'])
    home_page.click_search_button()
    
    result_message = home_page.get_search_result_message()

    with allure.step("Результат: " + result_message):
        assert result_message == "Результаты поиска не найдены, и элемент для отображения пустого результата отсутствует."