# final_project

## Дипломная работа по курсу - Автоматизация тестирования на Python

### Уточнения по работе
Для написания UI-тестов выбрана только одна функция — проверка поля "Поиск". Это обусловлено тем, что для остальных выбранных проверок на сайте "Читай-город" авторизация возможна только по номеру телефона с использованием СМС-кода.

API-тесты выполнены методами GET, POST, DELETE и PATCH. Данные для тестирования были взяты из функционального тестирования API (backend). Для метода GET написаны как позитивный, так и негативный сценарии.

Перед запуском теста нужно обновить токен в файле test_config.ini.

### Финальный проект по ручному тестированию
https://possible-bolt-045.notion.site/ea4f5376189f4060a39cf01941249492?pvs=4

### Шаги:
1. Склонировать проект 'git clone https://github.com/Mimzaaa/FP_ui_api_pytest.git'
2. Установить зависимости 'pip install -r requirements.txt'
3. Запустить тесты 'pytest --alluredir=./allure-results'
4. Сгенерировать отчет 'allure generate allure-results -o allure-report'
5. Открыть отчет 'allure serve allure-results'

### Стек:
- pytest
- selenium
- webdriver manager
- requests
- allure
- config
- configparser
- json

### Струткура:
- ./test - тесты
- ./pages - описание страниц
- ./configuration - провайдер настроек
    - test_config.ini - настройки для тестов
- ./testdata - провайдер тестовых данных
    - test_data.json
- ./requirements.txt - зависимости

### Полезные ссылки:
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)
- [Про configparser](https://docs.python.org/3/library/configparser.html#module-configparser)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)



final_project
- ./configuration - провайдер настроек
 - ConfigProvider.py
- ./pages - описание страниц
 - api_class.py
 - ui_class.py
- ./testdata - провайдер тестовых данных
 - DataProvider.py
- ./test - тесты
 - сonftest.py
 - tets_api.py
 - test_ui.py
- ./.gitignore
- ./conf.ini
- ./pytest.ini
- ./README.md
- ./test_config.ini - настройки для тестов
- ./test_data.json
- ./requirements.txt - зависимости