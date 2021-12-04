import requests


class MorseCodeData:
    """
    This class will search and structure morse code data.
    """

    def __init__(self):
        self.encode_api_end_point = 'http://www.morsecode-api.de/encode'
        self.decode_api_end_point = 'http://www.morsecode-api.de/decode'

    def get_morse_code(self, string):
        """
        This function returns encoded morse code from the api.
        :param string:
        :return:
        """
        parameters = {
            'string': string
        }
        connection = requests.get(url=self.encode_api_end_point, params=parameters)
        return connection.text

    def get_text(self, string):
        """
        This function returns the decoded message from the api
        :param string:
        :return:
        """
        parameters = {
            'string': string,
        }
        connection = requests.get(url=self.decode_api_end_point, params=parameters)
        return connection.text
