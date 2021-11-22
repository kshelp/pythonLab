# Q4 다음과 같은 내용을 지닌 파일 test.txt가 있다. 
# 이 파일의 내용 중 'java'라는 문자열을 'python'으로 바꾸어서 
# 저장해 보자.
'''
Life is too short
you need java
'''
f = open('./ch06_io/test.txt', 'r')
body = _____________ # test.txt 파일의 내용을 body 변수에 저장
f.close()
body = _______________________ # body 문자열에서 'java'를 'python'으로 변경
f = open('./ch06_io/test.txt', _____) # 파일을 쓰기 모드로 다시 실행
f.write(body)
f.close()

