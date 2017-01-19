from unittest.mock import patch
from nose import tools

from qaamus2.scraper import MunawwirScraper
from qaamus2.models.munawwir_berhub_collections import MunawwirBerhubModelCollections
from qaamus2.models.munawwir import MunawwirModel
from tests.config import html_markup


RESPONSE = html_markup('source/lari.html')

@patch('qaamus2.scraper.requests.get')
def test_response(obj):
    obj.return_value.text = RESPONSE

    munawwir = MunawwirScraper('lari')

    tools.eq_(RESPONSE, munawwir.response)

@patch('qaamus2.scraper.requests.get')
def test_check_pilihan(obj):
    tools.ok_(MunawwirScraper.check_pilihan('munawwir'))
