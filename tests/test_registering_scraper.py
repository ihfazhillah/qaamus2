from nose import tools

from qaamus2 import Qaamus


def test_qaamus_empty_scraper():
    tools.eq_(Qaamus.scrapers, [])

@tools.raises(TypeError)
def test_qaamus_register_scraper_failed():
    class BukanScraper: pass
    Qaamus.register_scraper(BukanScraper)
