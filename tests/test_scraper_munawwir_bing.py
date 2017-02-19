"""Test ini berisi test bilamana hasil utama yang ditampilkan
qaamus.com adalah dari bing translator"""
from unittest.mock import patch
from nose import tools

from qaamus2.scraper import MunawwirScraper
from tests.config import html_markup

RESPONSE = html_markup('source/nikah.html')

@patch('qaamus2.scraper.requests.get')
def test_response(req_mock):
    req_mock.return_value.text = RESPONSE

    nikah = MunawwirScraper('nikah')

    tools.eq_(nikah.response, RESPONSE)
