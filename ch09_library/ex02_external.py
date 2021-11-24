# 외장 함수
# glob은 특정 디렉토리에 있는 파일 이름 모두를 알아야 할때 사용한다.
import glob
print(glob.glob("c:\\Windows\\t*"))
'''
['c:\\Windows\\TAPI', 'c:\\Windows\\Tasks', 'c:\\Windows\\Temp', 'c:\\Windows\\tracing', 'c:\\Windows\\twain_32', 'c:\\Windows\\twain_32.dll']
'''


# webbrowser
import webbrowser
webbrowser.open("http://www.naver.com")
