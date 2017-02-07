from qaamus2.scraper import BaseScraper


class Qaamus(object):
    scrapers = []

    @staticmethod
    def register_scraper(scraper):

        if not issubclass(scraper, BaseScraper):
            raise TypeError("%s bukan subclass dari BaseScraper" % scraper.__name__)

        Qaamus.scrapers.append(scraper)
