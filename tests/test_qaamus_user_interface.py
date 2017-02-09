from qaamus2 import Qaamus
from qaamus2.models.munawwir import MunawwirModel
from qaamus2.models.pegon import PegonModel
from qaamus2.models.angka import AngkaModel

from nose import tools
from unittest.mock import patch
from tests.config import html_markup

ANGKA = html_markup('source/2017.html')
PEGON = html_markup('source/suharto.html')
MUNAWWIR = html_markup('source/lari.html')


def test_qaamus_scraper():
    tools.eq_(len(Qaamus.scrapers), 3)


@patch('qaamus2.scraper.requests.get')
def test_pegon_scraper(req_mock):
    req_mock.return_value.text = PEGON
    pegon = Qaamus(layanan='pegon').terjemah(indo='suharto')
    tools.ok_(isinstance(pegon.hasil(), PegonModel))

@patch('qaamus2.scraper.requests.get')
def test_angka_scraper(req_mock):
    req_mock.return_value.text = ANGKA
    angka = Qaamus(layanan='angka').terjemah(indo=2017)
    tools.ok_(isinstance(angka.hasil(), AngkaModel))

@patch('qaamus2.scraper.requests.get')
def test_munawwir_scraper(req_mock):
    req_mock.return_value.text = MUNAWWIR
    angka = Qaamus(layanan='munawwir').terjemah(indo='lari')
    tools.ok_(isinstance(angka.hasil(), MunawwirModel))

@patch('qaamus2.scraper.requests.get')
def test_angka_scraper(req_mock):
    req_mock.return_value.text = ANGKA
    angka = Qaamus(layanan='angka').terjemah(indo=2017, page=2)
    tools.ok_(isinstance(angka.hasil(), AngkaModel))
