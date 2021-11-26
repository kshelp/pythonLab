# 데이터 찾고 추출하기
from bs4 import BeautifulSoup

html = """<html><body><div><span>\
        <a href=http://www.naver.com>naver</a>\
        <a href=https://www.google.com>google</a>\
        <a href=http://www.daum.net>daum</a>\
        </span></div></body></html>"""

# BeaultifulSoup를 이용해 HTML 소스를 파싱
soup = BeautifulSoup(html, 'lxml')
print(soup)
'''
<html><body><div><span> <a href="http://www.naver.com">naver</a> <a href="https://www.google.com">google</a> <a href="http://www.daum.net">daum</a> </span></div></body></html>
PS D:\dev\workspace\python> 
'''

print(soup.prettify())
'''
<html>
 <body>
  <div>
   <span>
    <a href="http://www.naver.com">
     naver
    </a>
    <a href="https://www.google.com">
     google
    </a>
    <a href="http://www.daum.net">
     daum
    </a>
   </span>
  </div>
 </body>
</html>
'''

print(soup.find('a'))
# <a href="http://www.naver.com">naver</a>

print(soup.find('a').get_text())
# naver

print(soup.find_all('a'))
'''
[<a href="http://www.naver.com">naver</a>, <a href="https://www.google.com">google</a>, <a href="http://www.daum.net">daum</a>]
'''

site_names = soup.find_all('a')
for site_name in site_names:
    print(site_name.get_text())



