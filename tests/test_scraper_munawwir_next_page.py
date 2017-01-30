from unittest.mock import patch, PropertyMock
from nose import tools

from qaamus2.scraper import MunawwirScraper
from qaamus2.models.munawwir_berhub_collections import MunawwirBerhubModelCollections
from qaamus2.models.munawwir_berhub import MunawwirBerhubModel
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


@tools.raises(IndexError)
@patch('qaamus2.scraper.requests.get')
@patch('qaamus2.scraper.MunawwirScraper.current_page', new_callable=PropertyMock)
def test_next_page_kalau_sudah_di_ujung(scraper_mock, resp_mock):
    resp_mock.return_value.text = RESPONSE

    # instance = scraper_mock
    # instance.current_page.return_value = 4

    scraper_mock.return_value = 4


    page_four = MunawwirScraper('lari')
    # page_four.current_page = MagicMock(return_value=4)

    tools.eq_(page_four.current_page, 4)


    page_four.next_page()



@patch('qaamus2.scraper.requests.get')
def test_hasil_next_page_berhub(resp_mock):
    # reponse pertama
    resp_mock.return_value.text = RESPONSE

    page_one = MunawwirScraper('lari')

    tools.eq_(page_one.current_page, 1)

    # response kedua

    resp_mock.return_value.text = RESPONSE2

    page_two = page_one.next_page()

    expected = MunawwirBerhubModel(indo='lari berantai', 
                                   arab='عَدْوٌ أَو جَرْيٌ بِتَسَلْسُلٍ', 
                                   url='http://qaamus.com/indonesia-arab/lari+berantai/1')

    tools.eq_(len(page_two.berhubungan), 10)
    tools.eq_(next(page_two.berhubungan).__dict__, expected.__dict__)
    tools.ok_(isinstance(page_two.berhubungan, MunawwirBerhubModelCollections))



