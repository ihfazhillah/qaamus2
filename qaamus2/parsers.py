"""Module parser"""
from qaamus2 import patterns


class Parser(object):
    """Parser objek, 

    html_source: text dari html
    """

    def __init__(self, html_source):
        self.html_source = html_source

    def utama(self, strip_tags=True):
        """Proses Arti utama,

        param optional:
            strip_tags bool 

        return:
            BILA HASIL UTAMA ADA 3 ELEMENT
                tuple berisi 3 item, index pertama arab, kedua cara baca, ketiga source
                bila strip_tags True maka tags akan dihilangkan, dan whitespaces di kanan
                dan kiri juga dihilangkan,
                else maka akan ditampilkan bersama tag

                (Ini berhasil bila yang dicari terdapat di kamus)
            BILA HASIL UTAMA ADA 2 ELEMENT
                ini terjadi bila hasil utama didapatkan dari bing translator.
                maka akan mengembalikan tuple berisi 2 item. index 0 adalah arab, dan 1 adalah
                source
            BILA HANYA SATU
                string
        """
        hasil = patterns.IDAR.search(self.html_source)

        if hasil:
            hasil = hasil.groups()

            if strip_tags:
                return tuple(self.strip_tags(x) for x in hasil)

            return hasil

        hasil = patterns.IDAR_BING.search(self.html_source)

        if hasil:
            hasil = hasil.groups()

            if strip_tags:
                return tuple(self.strip_tags(x) for x in hasil)
            return hasil

        return patterns.ANGKA_PEGON.search(self.html_source).group(1).strip()

    def berhubungan(self, strip_tags=True):
        """Proses arti berhubungan

        param optional:
            strip_tags bool

        return generator expr
               berisi tuple dengan tiga item:
                    1. url
                    2. indo
                    3. arab
                dan bila tidak ditemukan akan raise StopIteration
        """
        hasil = patterns.BERHUBUNGAN.finditer(self.html_source)

        hasil_gen = (x.groups() for x in hasil)

        if strip_tags:
            for i in hasil_gen:
                yield tuple(self.strip_tags(x) for x in i)
        
        for i in hasil_gen:
            yield i

    @classmethod
    def strip_tags(cls, to_strip):
        """class method: strip_tags
        Menghilangkan tags

        param to_strip : yang akan dihilangkan tag nya, juga 
                         whitespaces yang ada dikanan atau kiri

        return str
        """
        return patterns.TAGS.sub('', to_strip).strip()

    @property
    def has_pagination(self):
        """Return true if page has pagination,
        else, return False"""
        if patterns.PAGINATION.search(self.html_source):
            return True
        return False

    @property
    def pages(self):
        """return list of pages yang ada di pagination,
        list, urut dari yang terkecil sampai yang terbesar (berdasarkan page)"""
        pages = [x.group(1) for x in patterns.PAGINATION_URL.finditer(self.html_source)]
       
        if len(pages) == 0:
            return None
        pages.append(patterns.PAGE_IN_URL.sub(str(self.current_page), pages[0]))

        return sorted(pages,
                      key=lambda page: int(patterns.PAGE_IN_URL.search(page).group()))

    @property
    def current_page(self):
        """Return int page sekarang"""
        cur_page = patterns.CURRENT_PAGE.search(self.html_source)

        if cur_page:
            return int(cur_page.group(1))
        return 1
