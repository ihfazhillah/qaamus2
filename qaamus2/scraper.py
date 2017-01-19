import requests
from qaamus2.models.angka import AngkaModel
from qaamus2.parsers import Parser


class AngkaScraper(object):
    
    def __init__(self, indo):
        self.indo = indo
        self.url = "http://qaamus.com/terjemah-angka/{}/angka".format(indo)
        self.response = self.get_response(indo)

    def get_response(self, indo):
        resp = requests.get(self.url)
        resp.encoding = 'cp1256'
        return resp.text

    def hasil(self):
        parser = Parser(self.response)
        utama = parser.utama()
        return AngkaModel(self.indo, utama, self.url)

    @classmethod
    def check_pilihan(self, pilihan):
        return pilihan == 'angka'



