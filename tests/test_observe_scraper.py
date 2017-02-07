from qaamus2 import Qaamus
from nose import tools, with_setup
from qaamus2.scraper import AngkaScraper, PegonScraper

def test_get_angka_scraper():
    angka = Qaamus('angka', 1234)
    tools.ok_(angka.get_scraper(), AngkaScraper)

@tools.raises(ValueError)
def test_layanan_tidak_ditemukan():
    Qaamus('arar', 1234).get_scraper()

#: TODO
#: tampilkan daftar layanan ketika layanan tidak ditemukan
#: kita ubah di file scraper
