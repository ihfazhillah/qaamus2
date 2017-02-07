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
    pegon = Qaamus(layanan='pegon')(indo='suharto')
    tools.ok_(isinstance(pegon, PegonModel))
