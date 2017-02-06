import requests
from qaamus2.models.angka import AngkaModel
from qaamus2.models.pegon import PegonModel
from qaamus2.parsers import Parser
from qaamus2.models.munawwir_berhub_collections import MunawwirBerhubModelCollections
from qaamus2.models.munawwir_berhub import MunawwirBerhubModel
from qaamus2.models.munawwir import MunawwirModel


ANGKA_URL = "http://qaamus.com/terjemah-angka/{}/angka"
PEGON_URL = "http://qaamus.com/terjemah-nama/{}"
MUNAWWIR_URL = "http://qaamus.com/indonesia-arab/{}/{}"


def request_get(url):
    resp = requests.get(url)
    resp.encoding = 'cp1256'
    return resp.text


class BaseScraper(object):
    url = None
    parser = Parser
    model = None

    def __init__(self, indo, page=1):
        self.url = self.url.format(indo, page)
        self.indo = indo
        self.response = request_get(self.url)

    def hasil(self):
        parser = self.parser(self.response)
        utama = parser.utama()

        if isinstance(utama, str):
            return self.model(self.indo, utama, self.url)
        else:
            arab, baca, source = utama
            return self.model(indo=self.indo,
                              arab=arab,
                              baca=baca,
                              sumber=source,
                              url=self.url,
                              berhubungan=self.berhubungan)


class AngkaScraper(BaseScraper):

    url = ANGKA_URL
    model = AngkaModel

    @classmethod
    def check_pilihan(self, pilihan):
        return pilihan == 'angka'


class PegonScraper(BaseScraper):

    url = PEGON_URL
    model = PegonModel

    @classmethod
    def check_pilihan(cls, pilihan):
        return pilihan == 'pegon'

class MunawwirScraper(BaseScraper):
 
    url = MUNAWWIR_URL
    model = MunawwirModel
 
    @classmethod
    def check_pilihan(cls, pilihan):
        return pilihan == 'munawwir'

    @property
    def berhubungan(self):
        parser = Parser(self.response)
        berhubungan = parser.berhubungan()
        berhubungan_iter = (MunawwirBerhubModel(x[1], x[2], x[0]) for x in berhubungan)

        return MunawwirBerhubModelCollections(berhubungan_iter)

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
