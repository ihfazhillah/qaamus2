from nose import tools
from qaamus2 import parsers
from tests.config import html_markup

FIXTURE = html_markup('source/nikah.html')


def test_dapatkan_hasil_utama():
    parsed = parsers.Parser(FIXTURE)
    utama_expected = ('رخصة الزواج', '*Diterjemahkan dengan Bing Translator')

    tools.eq_(utama_expected, parsed.utama())
