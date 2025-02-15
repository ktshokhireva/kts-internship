from endpoints.base_endpoint import BaseRequest
from models.advertisement import Advertisement
import requests

class SellerAdvertisementsRequest(BaseRequest):
    seller_advertisements: [Advertisement] = []

    def request_advertisements_of_seller(self, seller_id: int):
        """
        Запросить список объявлений у продавца с ID
        :param seller_id: ID продавца
        """

        seller_advertisements_url = f"{self.base_url}/api/1/{seller_id}/item"
        self.response = requests.get(seller_advertisements_url)
        if self.response.status_code == 200:
            for advertisement in self.json:
                self.seller_advertisements.append(Advertisement(advertisement))

    @property
    def advertisements_count(self):
        """
        Кол-во объявлений у продавца
        :return: кол-во объявлений
        """

        return len(self.seller_advertisements)

    def __find_advertisement_with(self, title: str, price: int, seller_id: int):
        """
        Найти объявление у продавца с указанными параметрами
        :param title: Название объявления
        :param price: Цена объявления
        :param seller_id: ID продавца
        :return: Объявление или None, если ничего не найдено
        """

        for advertisement in self.seller_advertisements:
            if advertisement.seller_id == seller_id and advertisement.price == price and advertisement.title == title:
                return advertisement
        return None

    def __advertisement_with(self, advertisement_id: str):
        """
        Найти объявление у продавца c указанным ID
        :param advertisement_id: ID объявления
        :return: Объявление или None, если ничего не найдено
        """

        for advertisement in self.seller_advertisements:
            if advertisement.advertisement_id == advertisement_id:
                return advertisement
        return None


    def assert_seller_has_advertisement_with(self, title: str, price: int, seller_id: int):
        """
        Проверить, что у продавца есть объявление с указанными параметрами
        :param title: Название объявления
        :param price: Цена объявления
        :param seller_id: ID продавца
        """

        advertisement = self.__find_advertisement_with(title, price, seller_id)
        assert advertisement is not None, f'Объявление с параметрами name: {title}, price: {price}, seller_id: {seller_id} - не найдено'

    def assert_seller_has_advertisement_with_id(self, advertisement_id: str):
        """
        Проверить, что у продавца есть объявление с указанным ID
        :param advertisement_id: ID объявления
        """

        advertisement = self.__advertisement_with(advertisement_id)
        assert advertisement is not None, f'Объявление с id: {advertisement_id} - не найдено'