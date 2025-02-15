class Statistic:
    __info: dict = None

    def __init__(self, info):
        self.__info = info

    @property
    def contacts(self):
        return self.__info['contacts']

    @property
    def likes(self):
        return self.__info['likes']

    @property
    def views_count(self):
        return self.__info['viewCount']