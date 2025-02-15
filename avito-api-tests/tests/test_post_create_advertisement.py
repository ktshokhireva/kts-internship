from endpoints.post_create_advertisement import CreateAdvertisementRequest
import pytest


# success ✅
def test_advertisement_creation_code_is_200():
    # Шаг 1: создать объявление
    creation_request = CreateAdvertisementRequest()
    creation_request.create_advertisement()

    # Проверка: код ответа - 200
    creation_request.assert_response_status_code_is(200)


# success ✅
def test_negative_advertisement_creation_code_is_400():
    # Шаг 1: создать объявление с неправильным типом данных
    creation_request = CreateAdvertisementRequest()
    creation_request.create_advertisement_with(title='title', seller_id='112', price='222')

    # Проверка: код ответа - 400
    creation_request.assert_response_status_code_is(400)