from qaamus2.scraper import BaseScraper


class Qaamus(object):
    scrapers = []

    def __init__(self, layanan, indo):
        self.layanan = layanan
        self.indo = indo

    def get_scraper(self):
        for scraper in Qaamus.scrapers:
            if scraper.check_pilihan(self.layanan):
                return scraper

        raise ValueError("Layanan %s tidak ditemukan" % self.layanan)

    @staticmethod
    def register_scraper(scraper):

        if not issubclass(scraper, BaseScraper):
            raise TypeError("%s bukan subclass dari BaseScraper" % scraper.__name__)


        if scraper not in Qaamus.scrapers:
            Qaamus.scrapers.append(scraper)



