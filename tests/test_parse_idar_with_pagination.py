from os import path
from nose import tools, with_setup
from qaamus2 import parsers

THE_DIR = path.dirname(__file__)

with open(path.join(THE_DIR, 'source/lari.html'), 'r') as html:
    HTML_FIXTURE = html.read()

def test_init():
    assert 'nama' in HTML_FIXTURE


def test_utama_without_param():
    parser = parsers.Parser(HTML_FIXTURE)
    hasil = ('عَدْوٌ ، جَرْيٌ ، عَدَا - يَعْدُوْ ، جَرَى - يَجْرِي',
             "adwun, jaryun, 'adaa - ya'duu, jaroo - yajrii",
             'Data diambil dari Kamus Al-Munawwir Edisi Indonesia Arab pada halaman 499')
    tools.eq_(parser.utama(), hasil)

def test_utama_strip_tags_true():
    parser = parsers.Parser(HTML_FIXTURE)
    hasil = ('عَدْوٌ ، جَرْيٌ ، عَدَا - يَعْدُوْ ، جَرَى - يَجْرِي',
             "adwun, jaryun, 'adaa - ya'duu, jaroo - yajrii",
             'Data diambil dari Kamus Al-Munawwir Edisi Indonesia Arab pada halaman 499')
    tools.eq_(parser.utama(strip_tags=True), hasil)

def test_utama_strip_tags_false():
    parser = parsers.Parser(HTML_FIXTURE)
    hasil = ('عَدْوٌ ، جَرْيٌ ، عَدَا - يَعْدُوْ ، جَرَى - يَجْرِي ',
             'adwun, jaryun, \'ad<span style="color:blue;text-decoration: underline;font-style:italic;font-weight:bold;">aa</span> - ya\'d<span style="color:blue;text-decoration: underline;font-style:italic;font-weight:bold;">uu</span>, jar<span style="color:blue;text-decoration: underline;font-style:italic;font-weight:bold;">oo</span> - yajr<span style="color:blue;text-decoration: underline;font-style:italic;font-weight:bold;">ii</span>',
             'Data diambil dari Kamus Al-Munawwir Edisi Indonesia Arab pada halaman <strong>499</strong> ')
    tools.eq_(parser.utama(strip_tags=False), hasil)

def test_strip_tags():
    text = "<a>hallo </a></br><script/>"
    hasil = "hallo"
    tools.eq_(hasil, parsers.Parser.strip_tags(text))

def test_berhubungan_without_param():
    parser = parsers.Parser(HTML_FIXTURE)
    hasil = ('http://qaamus.com/indonesia-arab/Lari+berjingkrak-jingkrak/1',
             'lari berjingkrak-jingkrak',
             'خَاضَ - يَخُوْضُ الجَوَادُ فِـي الـمَيْدَانِ')
    tools.eq_(next(parser.berhubungan()), hasil)

def test_berhubungan_strip_tags_true():
    parser = parsers.Parser(HTML_FIXTURE)
    hasil = ('http://qaamus.com/indonesia-arab/Lari+berjingkrak-jingkrak/1',
             'lari berjingkrak-jingkrak',
             'خَاضَ - يَخُوْضُ الجَوَادُ فِـي الـمَيْدَانِ')
    tools.eq_(next(parser.berhubungan(strip_tags=True)), hasil)

def test_berhubungan_strip_tags_false():
    parser = parsers.Parser(HTML_FIXTURE)
    hasil = ('http://qaamus.com/indonesia-arab/Lari+berjingkrak-jingkrak/1',
             'lari berjingkrak-jingkrak',
             '<div>خَاضَ - يَخُوْضُ الجَوَادُ فِـي الـمَيْدَانِ </div>')
    tools.eq_(next(parser.berhubungan(strip_tags=False)), hasil)

def test_has_pagination_true():
    parser = parsers.Parser(HTML_FIXTURE)
    tools.eq_(parser.has_pagination, True)

def test_has_pagination_false():
    pass

def test_pages():
    parser = parsers.Parser(HTML_FIXTURE)
    page_url = 'http://qaamus.com/indonesia-arab/lari/4'
    tools.eq_(page_url, parser.pages[-1])
    tools.eq_(4, len(parser.pages))

def test_current_page():
    parser = parsers.Parser(HTML_FIXTURE)
    tools.eq_(1, parser.current_page)

# found bug
def test_pages_with_plus_sign_in_the_url():
    with open(path.join(THE_DIR, 'source/rumah+sakit.html'), 'r') as f:
        html = f.read()

    parser = parsers.Parser(html)
    tools.eq_(len(parser.pages), 5)
    print(max(parser.pages))
    page_url = 'http://qaamus.com/indonesia-arab/rumah+sakit/4'
    tools.eq_(page_url, parser.pages[3])
