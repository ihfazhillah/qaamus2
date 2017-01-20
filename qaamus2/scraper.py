import requests
from qaamus2.models.angka import AngkaModel
from qaamus2.models.pegon import PegonModel
from qaamus2.parsers import Parser
from qaamus2.models.munawwir_berhub_collections import MunawwirBerhubModelCollections
from qaamus2.models.munawwir_berhub import MunawwirBerhubModel
from qaamus2.models.munawwir import MunawwirModel

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


class PegonScraper(object):

    def __init__(self, indo):
        self.indo = indo
        self.url = "http://qaamus.com/terjemah-nama/{}".format(indo)
        self.get_response()
        # self.response = None

    def get_response(self):
        resp = requests.get(self.url)
        resp.encoding = 'cp1256'
        self.response = resp.text

    def hasil(self):
        parser = Parser(self.response)
        utama = parser.utama()
        return PegonModel(self.indo, utama, self.url)

    @classmethod
    def check_pilihan(cls, pilihan):
        return pilihan == 'pegon'

class MunawwirScraper(object):
    def __init__(self, indo):
        self.indo = indo
        self.url = "http://qaamus.com/indonesia-arab/{}/1".format(indo)
        self.get_response()

    def get_response(self):
        resp = requests.get(self.url)
        self.encoding = 'cp1256'
        self.response = resp.text

    @classmethod
    def check_pilihan(cls, pilihan):
        return pilihan == 'munawwir'

    @property
    def berhubungan(self):
        parser = Parser(self.response)
        berhubungan = parser.berhubungan()
        berhubungan_iter = (MunawwirBerhubModel(x[1], x[2], x[0]) for x in berhubungan)

        return MunawwirBerhubModelCollections(berhubungan_iter)

    def hasil(self):
        parser = Parser(self.response)
        arab, baca, source = parser.utama()

        return MunawwirModel(indo=self.indo,
                             arab=arab,
                             baca=baca,
                             sumber=source,
                             url=self.url,
                             berhubungan=self.berhubungan)
