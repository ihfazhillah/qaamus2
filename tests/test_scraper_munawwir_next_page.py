from unittest.mock import patch
from nose import tools

from qaamus2.scraper import MunawwirScraper
from tests.config import html_markup


RESPONSE2 = html_markup('source/lari2.html')
RESPONSE = html_markup('source/lari.html')


@patch('qaamus2.scraper.requests.get')
def test_next_page(resp_mock):
    # response_pertama
    resp_mock.return_value.text = RESPONSE

    page_one = MunawwirScraper('lari')

    tools.eq_(RESPONSE, page_one.response)

    resp_mock.return_value.text = RESPONSE2

    page_two = page_one.next_page()

    tools.eq_(RESPONSE2, page_two.response)



