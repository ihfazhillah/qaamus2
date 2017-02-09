"""Modul qaamus2"""
from qaamus2.scraper import BaseScraper, AngkaScraper, PegonScraper, MunawwirScraper

class Qaamus(object):
    """Qaamus, python interface untuk berinteraksi dengan qaamus.com

    >>> from qaamus2 import Qaamus
    >>> pegon = Qaamus(layanan='pegon')

    untuk diperhatikan, layanan yang tersedia adalah:
        - pegon
        - angka
        - munawwir 

    >>> suharto = pegon(indo='suharto')
    >>> suharto.indo
    'suharto'

    that is... !!
    """
    scrapers = []

    def __init__(self, layanan):
        self.layanan = layanan
        self.scraper = self.get_scraper()

    def get_scraper(self):
        """dipakai internally, untuk mendapatkan scraper
        yang telah diregister berdasarkan layanan"""

        layanan_tersedia = []
        for scraper in Qaamus.scrapers:
            if scraper.check_pilihan(self.layanan):
                return scraper
            layanan_tersedia.append(scraper.layanan)

        raise ValueError("Layanan %s tidak ditemukan. Layanan tersedia: %s" 
                         % (self.layanan, ', '.join(layanan_tersedia)))

    @staticmethod
    def register_scraper(scraper):
        """Meregister scraper, scraper harus subclass dari BaseScraper"""

        if not issubclass(scraper, BaseScraper):
            raise TypeError("%s bukan subclass dari BaseScraper" % scraper.__name__)


        if scraper not in Qaamus.scrapers:
            Qaamus.scrapers.append(scraper)

    def terjemah(self, indo, page=1):
        """terjemahkan hasil
        indo kata yang mau di terjemahkan,
        page halaman, secara default halaman satu (hanya dipakai untuk munawwir)"""
        scraper = self.scraper
        return scraper(indo=indo, page=page)

Qaamus.register_scraper(AngkaScraper)
Qaamus.register_scraper(PegonScraper)
Qaamus.register_scraper(MunawwirScraper)
