====================
Qaamus
====================

Qaamus, pada dasarnya adalah library python yang digunakan untuk berinteraksi dengan website qaamus.com_. Tapi tidak menutup kemungkinan akan ditambahkan module dari beberapa website yang ada, yang lainnya.
.. _qaamus.com: http://qaamus.com 


Instalasi
==========

Sampai saat ini, belum saya upload ke pypi_. Hanya ada di github_.

Clone Github
---------------
::
    $ git clone https://github.com/ihfazhillah/qaamus2.git
    $ cd qaamus2
    $ python setup.py install

Menggunakan `pip`
-------------------
::
    $ pip install git+https://github.com/ihfazhillah/qaamus2.git

.. _pypi: http://
.. _github: https://github.com


Cara Penggunaaan
========================
Setelah selesai installasi, maka berikut ini adalah cara penggunaannya::
    >>> from qaamus2 import Qaamus
    >>> pegon = Qaamus('pegon')
    >>> suharto = pegon.terjemah('suharto').hasil()
    >>> suharto.indo, suharto.arab, suharto.url
    ('suharto', >>arabnya<<, >>urlnya<<)
    >>> angka = Qaamus('angka')
    >>> satuduatiga = angka.terjemah(123).hasil()
    >>> satuduatiga.indo, satuduatiga.arab, satuduatiga.url
    >>> 
    >>> munawwir = Qaamus('munawwir')
    >>> lari = munawwir.terjemah('lari')
    >>> lari.current_page
    1
    >>> lari2 = lari.next_page()
    >>> lari2.current_page
    2
    >>> lari.hasil()
    <MunawwirModel -lari->
    >>> lari.to_page(3).current_page
    3
    >>> lari.berhubungan
    <MunawwirBerhubunganModelCollections>
    >>> dir(lari)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'berhubungan', 'check_pilihan', 'current_page', 'has_pagination', 'hasil', 'indo', 'layanan', 'model', 'next_page', 'pages', 'parser', 'response', 'to_page', 'url']


