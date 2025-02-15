from endpoints.get_advertisement_info import AdvertisementInfoRequest
from endpoints.get_seller_advertisements import SellerAdvertisementsRequest
from endpoints.post_create_advertisement import CreateAdvertisementRequest
import pytest


# success ✅
def test_seller_list_increase_by_1_after_advert_creation():
    # Шаг 1. Запросить список объявлений продавца
    seller_id = 339999
    seller_advertisements_request = SellerAdvertisementsRequest()
    seller_advertisements_request.request_advertisements_of_seller(seller_id)
    seller_advertisements_request.assert_response_status_code_is(200)

    # Шаг 2. Посчитать кол-во объявлений
    advertisements_count_before = seller_advertisements_request.advertisements_count

    # Шаг 3. Создать объявление от этого продавца
    creation_request = CreateAdvertisementRequest()
    creation_request.create_advertisement_with(
        title=creation_request.default_title,
        seller_id=seller_id,
        price=creation_request.default_price
    )

    # Шаг 4. Запросить список объявлений продавца
    seller_advertisements_request.request_advertisements_of_seller(seller_id)
    seller_advertisements_request.assert_response_status_code_is(200)
    advertisements_count_after = seller_advertisements_request.advertisements_count

    # Проверка. Кол-во объявлений продавца должно было увеличиться на 1
    assert advertisements_count_after == advertisements_count_before + 1,\
        "Кол-во объявлений у продавца не изменилось после создания объявления с его ID"


# failed ❌
def test_seller_list_has_him_created_advertisement():
    # Шаг 1. Создать объявление от продавца с seller_id
    seller_id = 330030
    creation_request = CreateAdvertisementRequest()
    creation_request.create_advertisement_with(
        creation_request.default_title,
        seller_id,
        creation_request.default_price
    )

    # Шаг 2. Запросить список объявлений продавца
    seller_advertisements_request = SellerAdvertisementsRequest()
    seller_advertisements_request.request_advertisements_of_seller(seller_id)

    # Проверка. Код ответа - 200
    seller_advertisements_request.assert_response_status_code_is(200)

    # Проверка: В списке есть объявление с указанным id
    advertisement_id = creation_request.advertisement_id
    seller_advertisements_request.assert_seller_has_advertisement_with_id(advertisement_id)


# failed ❌
def test_adv_info_from_seller_list_is_correct():
    # Шаг 1. Создать объявление от продавца с seller_id
    seller_id = 330030
    creation_request = CreateAdvertisementRequest()
    creation_request.create_advertisement_with(
        creation_request.default_title,
        seller_id,
        creation_request.default_price
    )

    # Шаг 2. Запросить список объявлений продавца
    seller_advertisements_request = SellerAdvertisementsRequest()
    seller_advertisements_request.request_advertisements_of_seller(seller_id)

    # Проверка. Код ответа - 200
    seller_advertisements_request.assert_response_status_code_is(200)

    # Проверка: В списке есть объявление с указанными при создании данными
    seller_advertisements_request.assert_seller_has_advertisement_with(
        title=creation_request.default_title,
        seller_id=seller_id,
        price=creation_request.default_price
    )


# failed ❌
def test_adv_info_from_seller_list_is_same_as_created():
    # Шаг 1. Создать объявление от продавца с seller_id
    seller_id = 330030
    creation_request = CreateAdvertisementRequest()
    creation_request.create_advertisement_with(
        creation_request.default_title,
        seller_id,
        creation_request.default_price
    )

    # Шаг 2. Узнать фактические данные о созданном объявлении
    advertisement_id = creation_request.advertisement_id
    info_request = AdvertisementInfoRequest()
    info_request.request_advertisement_info_with(advertisement_id)

    # Проверка: код ответа - 200
    info_request.assert_response_status_code_is(200)

    # Шаг 3. Запросить список объявлений продавца
    seller_advertisements_request = SellerAdvertisementsRequest()
    seller_advertisements_request.request_advertisements_of_seller(seller_id)

    # Проверка. Код ответа - 200
    seller_advertisements_request.assert_response_status_code_is(200)

    # Проверка: В списке есть объявление с данными созданного объявления
    seller_advertisements_request.assert_seller_has_advertisement_with(
        title=info_request.advertisement.title,
        seller_id=info_request.advertisement.seller_id,
        price=info_request.advertisement.price
    )


# failed ❌
def test_negative_get_advertisements():
    # Шаг 1. Запросить список объявлений продавца с неправильным seller_id
    seller_advertisements_request = SellerAdvertisementsRequest()
    seller_advertisements_request.request_advertisements_of_seller(-1)

    # Проверка: код ответа - 400
    seller_advertisements_request.assert_response_status_code_is(400)