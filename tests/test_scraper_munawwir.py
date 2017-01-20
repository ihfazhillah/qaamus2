from unittest.mock import patch
from nose import tools

from qaamus2.scraper import MunawwirScraper
from qaamus2.models.munawwir_berhub_collections import MunawwirBerhubModelCollections
from qaamus2.models.munawwir_berhub import MunawwirBerhubModel
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


@patch('qaamus2.scraper.requests.get')
def test_berhubungan(obj):
    obj.return_value.text = RESPONSE

    munawwir = MunawwirScraper('lari')

    berhubungan = next(munawwir.berhubungan)

    expected = MunawwirBerhubModel('lari berjingkrak-jingkrak', 
                                   'خَاضَ - يَخُوْضُ الجَوَادُ فِـي الـمَيْدَانِ',
                                   'http://qaamus.com/indonesia-arab/Lari+berjingkrak-jingkrak/1').__dict__


    tools.eq_(berhubungan.__dict__, expected)
    tools.ok_(isinstance(munawwir.berhubungan, MunawwirBerhubModelCollections))

@patch('qaamus2.scraper.requests.get')
@patch.object(MunawwirScraper, 'berhubungan', spec=MunawwirBerhubModelCollections)
def test_hasil(munawwir_mock,obj):
    obj.return_value.text = RESPONSE

    berhubungan = MunawwirBerhubModelCollections((x for x in range(3)))
    munawwir_mock.return_value = berhubungan

    munawwir = MunawwirScraper('lari')

    expected = MunawwirModel(indo='lari', arab='عَدْوٌ ، جَرْيٌ ، عَدَا - يَعْدُوْ ، جَرَى - يَجْرِي',
                             baca="adwun, jaryun, 'adaa - ya'duu, jaroo - yajrii",
                             sumber='Data diambil dari Kamus Al-Munawwir Edisi Indonesia Arab pada halaman 499',
                             url='http://qaamus.com/indonesia-arab/lari/1',
                             berhubungan=munawwir_mock)

    tools.eq_(munawwir.hasil().__dict__, expected.__dict__)
