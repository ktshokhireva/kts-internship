class Advertisement:
    __info: dict = None

    def __init__(self, info):
        self.__info = info

    @property
    def title(self):
        return self.__info['name']

    @property
    def price(self):
        return self.__info['price']

    @property
    def seller_id(self):
        return self.__info['sellerId']

    @property
    def advertisement_id(self):
        return self.__info['id']