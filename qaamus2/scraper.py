"""Di sini tempat scraper module berada"""
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
    """helper requests.get untuk mereturn text
    dengan encoding yang benar yaitu : 'cp1256'
    """
    resp = requests.get(url)
    resp.encoding = 'cp1256'
    return resp.text


class BaseScraper(object):
    """Base scraper,

    Untuk class yang inherite dari class ini, 
    harus menentukan url dan model.

    url minimal dengan {} satu
    model salah satu dari AngkaModel, PegonModel, dan MunawwirModel

    bila model adalah MunawwirModel maka:
        - child class harus menentukan property bernama berhubungan 
          yang mengembalikan MunawwirBerhubModelCollections
    """
    url = None
    parser = Parser
    model = None

    def __init__(self, indo, page=1):
        self.url = self.url.format(indo, page)
        self.indo = indo
        self.response = request_get(self.url)

    def hasil(self):
        """Sementara tidak perli di override.
        return model yang telah di tentukan diatas"""
        parser = self.parser(self.response)
        utama = parser.utama()

        if not isinstance(utama, tuple):
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
    """Angka scraper

    contoh:
    >>> AngkaScraper(123).hasil().indo
    123
    """

    url = ANGKA_URL
    model = AngkaModel
    layanan = 'angka'

    @classmethod
    def check_pilihan(cls, pilihan):
        """untuk pilihan nanti di class observer (kalau tidak salah)"""
        return pilihan == cls.layanan


class PegonScraper(BaseScraper):
    """Pegon scraper

    contoh:
    >>> PegonScraper('suharto').hasil().indo
    suharto
    """

    url = PEGON_URL
    model = PegonModel

    @classmethod
    def check_pilihan(cls, pilihan):
        """untuk pilihan nanti di class observer (kalau tidak salah)"""
        return pilihan == 'pegon'

class MunawwirScraper(BaseScraper):
    """Munawwir scraper

    contoh:
    >>> munawwir = Munawwir('lari')

    anda pun juga dapat menentukan halaman
    >>> munawwir = Munawwir('lari', 1)

    """
 
    url = MUNAWWIR_URL
    model = MunawwirModel
 
    @classmethod
    def check_pilihan(cls, pilihan):
        """untuk pilihan nanti di class observer (kalau tidak salah)"""
        return pilihan == 'munawwir'

    @property
    def berhubungan(self):
        """return BerhubModelCollections berdasarkan self.response"""
        parser = Parser(self.response)
        berhubungan = parser.berhubungan()
        berhubungan_iter = (MunawwirBerhubModel(x[1], x[2], x[0]) for x in berhubungan)

        return MunawwirBerhubModelCollections(berhubungan_iter)

    @property
    def has_pagination(self):
        """Return true kalau punya pagination

        >>> munawwir.has_pagination
        True # kalau memang ada, kalau tidak ada jadi False
        """
        parser = Parser(self.response)

        return parser.has_pagination

    @property
    def current_page(self):
        """return integer, page sekarang

        >>> munawwir.current_page
        1
        """
        parser = Parser(self.response)

        return parser.current_page

    @property
    def pages(self):
        """return list of url pages di halaman sekarang

        >>> munawwir.pages[0]
        'http://qaamus.com/indonesia-arab/lari/1'
        """
        parser = Parser(self.response)

        return parser.pages

    def next_page(self):
        """return dirinya, dengan response yang sudah diubah

        >>> dua = munawwir.next_page()
        >>> dua.url
        'http://qaamus.com/indonesia-arab/lari/2'
        """

        if self.current_page == len(self.pages):
            raise IndexError("Ini sudah ujung halaman.")

        url = self.pages[self.current_page] # karena index mulai dari 0

        resp = request_get(url)

        self.response = resp

        return self

    def to_page(self, page):
        """return MunawwirScraper objek dengan page yang telah diubah

        >>> tiga = munawwir.to_page(3)
        >>> tiga.url
        'http://qaamus.com/indonesia-arab/lari/3'
        """
        return MunawwirScraper(indo=self.indo, page=page)
