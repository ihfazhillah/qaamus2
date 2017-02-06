from unittest.mock import patch
from nose import tools

from tests.config import html_markup
from qaamus2.scraper import MunawwirScraper


RESPONSE1 = html_markup('source/lari.html')
RESPONSE2 = html_markup('source/lari2.html')

URL = 'http://qaamus.com/indonesia-arab/{}/{}'


def test_default_page_is_one():
    m = MunawwirScraper('lari')
    tools.eq_(m.url, URL.format('lari', '1'))
