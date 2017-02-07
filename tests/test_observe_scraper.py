from qaamus2 import Qaamus
from nose import tools, with_setup
from qaamus2.scraper import AngkaScraper, PegonScraper

def test_get_angka_scraper():
    angka = Qaamus('angka')
    tools.ok_(angka.get_scraper(), AngkaScraper)

@tools.raises(ValueError)
def test_layanan_tidak_ditemukan():
    Qaamus('arar').get_scraper()

@tools.raises(ValueError)
def test_layanan_tidak_ditemukan_juga_ketika_sudah_jadi_instance():
    Qaamus('tidak')

#: TODO
#: tampilkan daftar layanan ketika layanan tidak ditemukan
#: kita ubah di file scraper
