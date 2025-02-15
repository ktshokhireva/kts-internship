from endpoints.get_advertisement_info import AdvertisementInfoRequest
from endpoints.post_create_advertisement import CreateAdvertisementRequest
import pytest


# failed ❌
def test_advertisement_info_is_correct():
    # Шаг 1: создать объявление
    creation_request = CreateAdvertisementRequest()
    creation_request.create_advertisement()

    # Шаг 2: запросить информацию об этом объявлении
    advertisement_id = creation_request.advertisement_id
    info_request = AdvertisementInfoRequest()
    info_request.request_advertisement_info_with(advertisement_id)

    # Проверка: код ответа - 200
    info_request.assert_response_status_code_is(200)

    # Проверка: все данные объявления совпадают с указанными
    info_request.assert_advertisement_price_is(creation_request.default_price)
    info_request.assert_advertisement_title_is(creation_request.default_title)
    info_request.assert_seller_id_is(creation_request.default_seller_id)


# success ✅
def test_negative_advertisement_info_code_is_400():
    # Шаг 1: запросить информацию об объявлении с неправильным id
    info_request = AdvertisementInfoRequest()
    info_request.request_advertisement_info_with('error')

    # Проверка: код ответа - 400
    info_request.assert_response_status_code_is(400)