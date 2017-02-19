"""Pattern lists"""
import re


IDAR = re.compile("""<div class=lateef2>(.+?)</div>.+<em.+?>(.+?)</em>.+?<div class="panel-footer">(.+?)</div>""")
IDAR_BING = re.compile("""<div class=lateef2>(.+?)</div>.+?<div class="panel-footer">(.+?)</div>""")
ANGKA_PEGON = re.compile("""<div class=lateef2>(.+?)</div>""")
BERHUBUNGAN = re.compile("""<td.+?><a href="(.+?)">(.+?)</a></td><td class="lateef".+?>(.+?</div>)</td>""")
TAGS = re.compile(r"<.+?>")
PAGINATION = re.compile(r"""http://qaamus\.com/indonesia-arab[\w\/]+?""")
PAGINATION_URL = re.compile(r"""<li> ?<a href='(http://qaamus\.com/indonesia-arab[\w+\/]+?) '>(?!Next)""")
PAGE_IN_URL = re.compile(r'\d+')
CURRENT_PAGE = re.compile(r'<a href=#>(\d+)</a>')
