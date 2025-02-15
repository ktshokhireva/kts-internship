from endpoints.base_endpoint import BaseRequest
from models.advertisement import Advertisement
import requests

class AdvertisementInfoRequest(BaseRequest):
    advertisement: Advertisement = None

    def request_advertisement_info_with(self, advertisement_id: str):
        advertisement_info_url = f"{self.base_url}/api/1/item/{advertisement_id}"
        self.response = requests.get(advertisement_info_url)
        if self.response.status_code == 200:
            self.advertisement = Advertisement(self.json[0])

    def assert_advertisement_title_is(self, title: str):
        assert self.advertisement.title == title, f'Название объявления не совпало с ОР: {title}, ФР: {self.advertisement.title}'

    def assert_advertisement_price_is(self, price: int):
        assert self.advertisement.price == price, f'Цена объявления не совпала с ОР: {price}, ФР: {self.advertisement.price}'

    def assert_seller_id_is(self, seller_id: int):
        assert self.advertisement.seller_id == seller_id, f'ID продавца не совпал с ОР: {seller_id}, ФР: {self.advertisement.seller_id}'