# 웹 페이지의 HTML 소스 갖고 오기
import requests
from requests.api import request

r = requests.get("https://www.google.co.kr")
print(r)
# <Response [200]>

print(r.text[0:100])
'''
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content
PS D:\dev\workspace\python>
'''

html = requests.get("https://www.google.co.kr").text
print(html[0:100])
'''
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content
'''