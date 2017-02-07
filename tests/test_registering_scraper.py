from nose import tools

from qaamus2 import Qaamus

def test_qaamus_empty_scraper():
    tools.eq_(Qaamus.scrapers, [])

@tools.raises(TypeError)
def test_qaamus_register_scraper_failed():
    class BukanScraper: pass
    Qaamus.register_scraper(BukanScraper)

def test_qaamus_register_scraper_berhasil():
    from qaamus2.scraper import AngkaScraper
    Qaamus.register_scraper(AngkaScraper)

    scrapers = Qaamus.scrapers

    tools.eq_(scrapers[0], AngkaScraper)

def test_qaamus_register_2_kali_tidak_nambahkan():
    from qaamus2.scraper import AngkaScraper
    Qaamus.register_scraper(AngkaScraper)
    Qaamus.register_scraper(AngkaScraper)

    scrapers = Qaamus.scrapers

    tools.eq_(len(scrapers), 1)
