import os
from unittest.mock import patch
from qaamus2.scraper import PegonScraper
from qaamus2.models.pegon import PegonModel
from nose import tools


THIS_PATH = os.path.dirname(__file__)
with open(os.path.join(THIS_PATH, 'source/suharto.html'), 'r') as f:
    PEGON_HTML = f.read()


@patch('qaamus2.scraper.requests.get')
def test_response(mock_obj):
    mock_obj.return_value.text = PEGON_HTML

    pegon = PegonScraper('suharto')

    tools.eq_(pegon.response, PEGON_HTML)

@patch('qaamus2.scraper.requests.get')
def test_hasil(mock_obj):
    mock_obj.return_value.text = PEGON_HTML

    pegon = PegonScraper('suharto')

    hasil = PegonModel('suharto', 'سوهارتو', 'http://qaamus.com/terjemah-nama/suharto').__dict__

    tools.eq_(hasil, pegon.hasil().__dict__)

@patch('qaamus2.scraper.requests.get')
def test_check_pilihan(mock_obj):
    tools.ok_(PegonScraper.check_pilihan('pegon'))
