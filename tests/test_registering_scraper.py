from nose import tools

from qaamus2 import Qaamus


def test_qaamus_empty_scraper():
    tools.eq_(Qaamus.scrapers, [])
