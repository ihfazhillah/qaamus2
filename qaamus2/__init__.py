
class Qaamus(object):
    scrapers = []

    def register_scraper(self, scraper):
        raise TypeError("%s bukan subclass dari BaseScraper" % scraper.__name__)
