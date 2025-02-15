from endpoints.base_endpoint import BaseRequest
from models.statistic import Statistic
import requests

class AdvertisementStatisticRequest(BaseRequest):
    __statistic: Statistic = None
    __advertisement_id: str = None

    def request_statistic_of_advertisement_with(self, advertisement_id: str):
        """
        Запросить статистику объявления с ID
        :param advertisement_id: ID объявления
        """

        self.__advertisement_id = advertisement_id
        advertisement_stats_url =  f"{self.base_url}/api/1/statistic/{advertisement_id}"
        self.response = requests.get(advertisement_stats_url)
        if self.response.status_code == 200:
            self.__statistic = Statistic(self.json[0])

    def assert_likes_exist(self):
        assert self.__statistic.likes is not None, f"Информация о лайках об-я {self.__advertisement_id} не найдена"

    def assert_contacts_exist(self):
        assert self.__statistic.contacts is not None, f"Информация о контактах об-я {self.__advertisement_id} не найдена"

    def assert_views_count_exists(self):
        assert self.__statistic.views_count is not None, f"Информация о просмотрах об-я {self.__advertisement_id} не найдена"