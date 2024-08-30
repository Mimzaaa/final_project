import requests
from pages.api_class import ApiReadCity
from testdata.DataProvider import DataProvider
import allure

@allure.title("Поиск книги с однословным правильным названием")
def test_search_product(api_client: ApiReadCity, data_provider: DataProvider):
    search_tests = data_provider.get_search_tests()
    for testdata in search_tests:
        phrase = testdata.get("api_search_phrases", [])[0]
        with allure.step(f"Поиск книги с фразой: {phrase}"):
            response = api_client.search_product(phrase)
            json_response = response.json()
            with allure.step("В теле ответа получен код статус 200"):
                assert response.status_code == 200, f"Ожидаемый код статус 200, но получили {response.status_code}"
            with allure.step("В теле ответа ключ 'transformedPhrase' содержит значение" + phrase):
                transformed_phrase = json_response['data']['attributes'].get('transformedPhrase', '').lower()
                assert phrase.lower() in transformed_phrase, f"Ожидаем '{phrase}' в transformedPhrase, но получили '{transformed_phrase}'"

@allure.title("Поиск книги с пустым полем")
def test_empty_search_phrase(api_client: ApiReadCity, data_provider: DataProvider):
    try:
        search_tests = data_provider.get_search_tests()
        for testdata in search_tests:
            phrase = testdata.get("api_search_phrases", [])[1]
            with allure.step(f"Поиск книги с пустой фразой: {phrase}"):
                response = api_client.search_product(phrase)
                assert False, "Ожидалась ошибка HTTP, но запрос выполнен успешно"
    except requests.exceptions.HTTPError as e:
        with allure.step("Проверка ошибки HTTP 400"):
            assert e.response.status_code == 400, f"Ожидаемый код статус 400, но получили {e.response.status_code}"

            json_response = e.response.json()
            assert "errors" in json_response, "Ожидалось 'errors' в ответе"
            
            error = json_response["errors"][0]
            assert error["code"] == "c1051bb4-d103-4f74-8988-acbcafc7fdc3", "Неожидаемый код ошибки"
            assert error["status"] == "400", "Неожидаемый статус в ответе"
            assert error["title"] == "Phrase обязательное поле", "Неожидаемая ошибка в названии"
            assert error["source"]["pointer"] == "GetSearchProductParams.Phrase", "Неожидаемый указатель источника ошибки"

@allure.title("Поиск книги с вводом только символов")
def test_search_invalid_phrase(api_client: ApiReadCity, data_provider: DataProvider):
    search_tests = data_provider.get_search_tests()
    for testdata in search_tests:
        try:
            phrase = testdata.get("api_search_phrases", [])[2]
            with allure.step(f"Поиск книги с некорректной фразой: {phrase}"):
                response = api_client.search_product(phrase)
                assert False, "Ожидалась ошибка HTTP, но запрос выполнен успешно"
        except requests.exceptions.HTTPError as e:
            with allure.step("Проверка ошибки HTTP 422"):
                assert e.response.status_code == 422
                response_data = e.response.json()
                assert "errors" in response_data
                assert len(response_data["errors"]) > 0
                
                error = response_data["errors"][0]
                assert error["code"] == "e91ae96b-2801-46ea-9fd2-416566122f11"
                assert error["status"] == "422"
                assert error["title"] == "Недопустимая поисковая фраза"

@allure.title("Добавление книги в закладку")
def test_add_bookmark(api_client: ApiReadCity, data_provider: DataProvider):
    book_id = data_provider.get_book_id()
    with allure.step(f"Добавление книги с ID: {book_id} в закладки"):
        response = api_client.add_bookmark(book_id)
        with allure.step("Получить в теле ответа код статус 201"):
            assert response.status_code in [200, 201], f"Ожидаемый статус код 200 или 201, но получили {response.status_code}"
            assert response.text == "", "Ожидаемое пустое тело ответа"

@allure.title("Удаление книги из вкладки закладки")
def test_remove_bookmark(api_client: ApiReadCity, data_provider: DataProvider):
    book_id = data_provider.get_book_id()
    with allure.step(f"Удаление книги с ID: {book_id} из закладок"):
        response = api_client.remove_bookmark(book_id)

        assert response.status_code in [200, 204], f"Ожидаемый статус код 200 или 204, но получили {response.status_code}"
        assert response.text == "", "Ожидаемое пустое тело ответа"

@allure.title("Изменение персональных данных")
def test_update_personal_data(api_client: ApiReadCity, data_provider: DataProvider):
    personal_data_tests = data_provider.get_personal_data_tests()
    assert len(personal_data_tests) > 0, "Данные для персональных тестов отсутствуют"

    personal_data = personal_data_tests[0]
    with allure.step("Изменение персональных данных"):
        response = api_client.update_personal_data(personal_data)
        json_response = response.json()

        assert response.status_code == 200, f"Ожидаемый статус код 200, но получили {response.status_code}"
        assert json_response["data"]["lastName"] == personal_data["lastName"], "Персональные данные в ответе не соответствуют ожидаемым данным"