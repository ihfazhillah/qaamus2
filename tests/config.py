import os

THIS_DIR = os.path.dirname(__file__)


def html_markup(filepath):
    """return string of html markup"""
    with open(os.path.join(THIS_DIR, filepath), 'r') as fp:
        return fp.read()
