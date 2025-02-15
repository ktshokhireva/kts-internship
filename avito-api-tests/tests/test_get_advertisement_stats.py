from endpoints.get_advertisement_stats import AdvertisementStatisticRequest
from endpoints.post_create_advertisement import CreateAdvertisementRequest
import pytest


# success ✅
def test_advertisement_stats_have_all_field():
    # Шаг 1: создать объявление
    creation_request = CreateAdvertisementRequest()
    creation_request.create_advertisement()

    # Шаг 2: запросить статистику по нему
    advertisement_id = creation_request.advertisement_id
    statistics_request = AdvertisementStatisticRequest()
    statistics_request.request_statistic_of_advertisement_with(advertisement_id)

    # Проверка: код ответа - 200
    statistics_request.assert_response_status_code_is(200)

    # Проверка: контакты, лайки и просмотры есть в ответе
    statistics_request.assert_contacts_exist()
    statistics_request.assert_likes_exist()
    statistics_request.assert_views_count_exists()


# success ✅
def test_negative_create_advertisement_stats():
    # Шаг 1: запросить информацию об объявлении с неправильным id
    statistics_request = AdvertisementStatisticRequest()
    statistics_request.request_statistic_of_advertisement_with('error')

    # Проверка: код ответа - 400
    statistics_request.assert_response_status_code_is(400)