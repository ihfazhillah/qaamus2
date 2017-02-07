from qaamus2 import Qaamus
from nose import tools
from qaamus2.scraper import AngkaScraper, PegonScraper

def setup_module():
    Qaamus.register_scraper(AngkaScraper)
    Qaamus.register_scraper(PegonScraper)

def teardown_module():
    Qaamus.scrapers = []

def test_get_angka_scraper():
    angka = Qaamus('angka', 1234)
    tools.ok_(angka.get_scraper(), AngkaScraper)

@tools.raises(ValueError)
def test_layanan_tidak_ditemukan():
    Qaamus('arar', 1234).get_scraper()
