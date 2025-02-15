from requests import Response


class BaseRequest:
    base_url = 'https://qa-internship.avito.com'

    response: Response

    @property
    def json(self):
        return self.response.json()

    def assert_response_status_code_is(self, code: int):
        """
        Проверить, совпадает ли код ответа с указанным
        :param code: Код ответа
        """
        assert self.response.status_code == code,\
            f'Код ответа {self.response.url} не совпал с ОР: {code}, ФР: {self.response.status_code}'