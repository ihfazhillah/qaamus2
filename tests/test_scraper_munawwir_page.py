from unittest.mock import patch
from nose import tools

from tests.config import html_markup
from qaamus2.scraper import MunawwirScraper


RESPONSE1 = html_markup('source/lari.html')
RESPONSE2 = html_markup('source/lari2.html')

URL = 'http://qaamus.com/indonesia-arab/{}/{}'


@patch('qaamus2.scraper.requests.get')
def test_default_page_is_one(request_mock):
    m = MunawwirScraper('lari')
    tools.eq_(m.url, URL.format('lari', '1'))


@patch('qaamus2.scraper.requests.get')
def test_munawwir_scraper_param_page(request_mock):
    m = MunawwirScraper('lari', page=2)
    tools.eq_(m.url, URL.format('lari', '2'))
