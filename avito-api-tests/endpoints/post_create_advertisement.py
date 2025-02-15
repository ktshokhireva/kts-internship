from endpoints.base_endpoint import BaseRequest
import requests

class CreateAdvertisementRequest(BaseRequest):

    default_title = "test"
    default_price = 3000
    default_seller_id = 330030

    def create_advertisement(self):
        """
        Делаем запрос на создание объявления значениями по умолчанию
        """

        self.create_advertisement_with(title=self.default_title, seller_id=self.default_seller_id, price=self.default_price)

    def create_advertisement_with(self, title, seller_id, price):
        """
        Делаем запрос на создание объявления
        :param title: Название объявления
        :param seller_id: ID продавца
        :param price: Цена объявления
        """

        request_body = {
            "sellerID": seller_id,
            "name": title,
            "price": price
        }

        url = f"{self.base_url}/api/1/item"
        self.response = requests.post(url, json=request_body)


    @property
    def advertisement_id(self):
        """
        Возвращаем ID объявления.
        :return: ID объявления строкой
        """
        status = self.json.get('status')
        advertisement_id = status.removeprefix('Сохранили объявление - ')
        return advertisement_id