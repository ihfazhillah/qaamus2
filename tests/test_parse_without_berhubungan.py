from nose import tools
from qaamus2 import parsers
from tests.config import html_markup

HTML_FIXTURE = html_markup('source/panahan.html')

def test_utama_without_param():
    parser = parsers.Parser(HTML_FIXTURE)
    hasil = ("رِمَايَةٌ بِالأَسْهُمِ و القِسِيّ",
             "rimaayatun bil ashumi wal qisiyyu",
             "Data diambil dari Kamus Al-Munawwir Edisi Indonesia Arab pada halaman 632")
    tools.eq_(parser.utama(), hasil)

def test_utama_dengan_param():
    parser = parsers.Parser(HTML_FIXTURE)
    hasil = ("رِمَايَةٌ بِالأَسْهُمِ و القِسِيّ",
             "rimaayatun bil ashumi wal qisiyyu",
             "Data diambil dari Kamus Al-Munawwir Edisi Indonesia Arab pada halaman 632")
    tools.eq_(parser.utama(strip_tags=True), hasil)

def test_utama_dengan_param_false():
    parser = parsers.Parser(HTML_FIXTURE)
    hasil = ("رِمَايَةٌ بِالأَسْهُمِ و القِسِيّ",
             'rim<span style="color:blue;text-decoration: underline;font-style:italic;font-weight:bold;">aa</span>yatun bil ashumi wal qisi<span style="color:red;font-weight:bold;">yy</span>u',
             "Data diambil dari Kamus Al-Munawwir Edisi Indonesia Arab pada halaman <strong>632</strong> ")
    tools.eq_(parser.utama(strip_tags=False), hasil)

@tools.raises(StopIteration)
def test_berhubungan_tidak_ditemukan():
    parser = parsers.Parser(HTML_FIXTURE)
    tools.eq_(next(parser.berhubungan()), None)
    tools.eq_(next(parser.berhubungan(False)), None)

def test_has_pagination_false():
    """sebetulnya disini ada pagination tapi
    hanya ditampilkan halaman satu,
    oleh karena itu saya force menjadi tidak ada"""
    parser = parsers.Parser(HTML_FIXTURE)
    tools.eq_(parser.has_pagination, False)

def test_pages():
    # tidak dapat
    parser = parsers.Parser(HTML_FIXTURE)
    tools.eq_(parser.pages, None)

def current_page():
    parser = parsers.Parser(HTML_FIXTURE)
    tools.eq_(parser.current_page, 1)
