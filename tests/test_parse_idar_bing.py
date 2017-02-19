from nose import tools
from qaamus2 import parsers
from tests.config import html_markup

FIXTURE = html_markup('source/nikah.html')


def test_dapatkan_hasil_utama():
    parsed = parsers.Parser(FIXTURE)
    utama_expected = ('رخصة الزواج', '*Diterjemahkan dengan Bing Translator')

    tools.eq_(utama_expected, parsed.utama())

def test_dapatkan_hasil_utama_strip_tags_false():
    parsed = parsers.Parser(FIXTURE)
    utama_expected = ('رخصة الزواج', '*Diterjemahkan dengan Bing Translator ')

    tools.eq_(utama_expected, parsed.utama(strip_tags=False))

def test_dapatkan_berhubungan():
    parsed = parsers.Parser(FIXTURE)

    berhubungan = parsed.berhubungan()

    next(berhubungan)

    akad = next(berhubungan)

    tools.eq_('akad nikah', akad[1])
