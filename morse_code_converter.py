from morse_code_data import MorseCodeData


class MorseCodeConverter:
    def __init__(self):
        """This class will get the data from MorseCodeData class and make changes to the data."""
        self.data = MorseCodeData()

    def encode(self, string):
        data = self.data.get_morse_code(string)
        code = data.split('"')[7]
        return code

    def decode(self, string):
        data = self.data.get_text(string)
        text = data.strip('{}').split('"')[3]
        return text


x = MorseCodeConverter()
