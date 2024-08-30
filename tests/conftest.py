import pytest
import allure
from selenium import webdriver
from pages.api_class import ApiReadCity
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


@pytest.fixture
def browser():
    with allure.step("Открыть браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.maximize_window()
        yield browser
   
    with allure.step("Закрыть браузер"):
        browser.quit()

"""Фикстура для создания клиента API"""
@pytest.fixture 
def api_client(config_provider):
    return ApiReadCity(config_provider)

"""Фикстура для предоставления конфигурации"""
@pytest.fixture
def config_provider():
    return ConfigProvider()

"""Фикстура для предоставления тестовых данных"""
@pytest.fixture
def data_provider():
    return DataProvider()

"""Фикстура для предоставления тестовых данных"""
@pytest.fixture()
def test_data():
    return DataProvider()