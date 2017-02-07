from qaamus2.scraper import BaseScraper, AngkaScraper, PegonScraper, MunawwirScraper

class Qaamus(object):
    scrapers = []

    def __init__(self, layanan):
        self.layanan = layanan
        self.scraper = self.get_scraper()

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

    def __call__(self, indo, page=1):
        scraper = self.scraper
        return scraper(indo=indo, page=page).hasil()

Qaamus.register_scraper(AngkaScraper)
Qaamus.register_scraper(PegonScraper)
Qaamus.register_scraper(MunawwirScraper)
