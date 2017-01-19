from nose import tools
from qaamus2 import parsers
from tests.config import html_markup

HTML_FIXTURE = html_markup('source/suharto.html')

def test_hasil_utama():
    parser = parsers.Parser(HTML_FIXTURE)
    hasil = "سوهارتو"
    tools.eq_(hasil, parser.utama())

@tools.raises(StopIteration)
def test_tidak_punya_berhubungan():
    parser = parsers.Parser(HTML_FIXTURE)
    next(parser.berhubungan())

def test_has_pagination_false():
    parser = parsers.Parser(HTML_FIXTURE)
    tools.eq_(parser.has_pagination, False)

def test_pages():
    parser = parsers.Parser(HTML_FIXTURE)
    tools.eq_(parser.pages, None)

def test_current_page():
    """meski dia tidak punya pagination class
    akan tetapi, setiap hasil tetap dihalaman 
    pertama kan?
    """
    parser = parsers.Parser(HTML_FIXTURE)
    tools.eq_(parser.current_page, 1)
