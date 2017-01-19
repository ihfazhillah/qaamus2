from unittest.mock import patch
from qaamus2.scraper import AngkaScraper
from qaamus2.models.angka import AngkaModel
from nose import tools
from tests.config import html_markup

RESPONSE_TEXT = html_markup('source/2017.html') 

@patch('qaamus2.scraper.requests.get')
def test_scrape_angka_response(mock_obj):
    mock_obj.return_value.text = RESPONSE_TEXT

    angka = AngkaScraper(2017)

    tools.eq_(angka.response, RESPONSE_TEXT)


@patch('qaamus2.scraper.requests.get')
def test_scrape_angka_hasil(mock_obj):

    mock_obj.return_value.text = RESPONSE_TEXT

    angka = AngkaScraper(2017)

    expected = AngkaModel(2017, 'الألفان و السابع عشر', 'http://qaamus.com/terjemah-angka/2017/angka').__dict__

    tools.eq_(expected, angka.hasil().__dict__)
    tools.ok_(isinstance(angka.hasil(), AngkaModel))

@patch('qaamus2.scraper.requests.get')
def test_scrape_angka_check_pilihan(mock_obj):
    tools.eq_(AngkaScraper.check_pilihan('angka'), True)
