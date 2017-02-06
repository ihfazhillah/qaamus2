import requests
from qaamus2.models.angka import AngkaModel
from qaamus2.models.pegon import PegonModel
from qaamus2.parsers import Parser
from qaamus2.models.munawwir_berhub_collections import MunawwirBerhubModelCollections
from qaamus2.models.munawwir_berhub import MunawwirBerhubModel
from qaamus2.models.munawwir import MunawwirModel


def request_get(url):
    resp = requests.get(url)
    resp.encoding = 'cp1256'
    return resp.text


class AngkaScraper(object):
    
    def __init__(self, indo):
        self.indo = indo
        self.url = "http://qaamus.com/terjemah-angka/{}/angka".format(indo)
        self.response = request_get(self.url)

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
        self.response = request_get(self.url)

    def hasil(self):
        parser = Parser(self.response)
        utama = parser.utama()
        return PegonModel(self.indo, utama, self.url)

    @classmethod
    def check_pilihan(cls, pilihan):
        return pilihan == 'pegon'

class MunawwirScraper(object):
    def __init__(self, indo, page=1):
        self.indo = indo
        self.url = "http://qaamus.com/indonesia-arab/{}/{}".format(indo, page)
        self.response = request_get(self.url)

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

    @property
    def has_pagination(self):
        parser = Parser(self.response)

        return parser.has_pagination

    @property
    def current_page(self):
        parser = Parser(self.response)

        return parser.current_page

    @property
    def pages(self):
        parser = Parser(self.response)

        return parser.pages

    def next_page(self):

        if self.current_page == len(self.pages):
            raise IndexError("Ini sudah ujung halaman.")

        url = self.pages[self.current_page] # karena index mulai dari 0

        resp = request_get(url)

        self.response = resp

        return self

    def to_page(self, page):
        return MunawwirScraper(indo=self.indo, page=page)
