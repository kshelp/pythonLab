# Q3 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 
# 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 
# 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
user_input = input("저장할 내용을 입력하세요: ")
f = open("./ch06_io/test.txt", ____)
f.write(____) ## 입력한 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입
f.write(user_input)
f.close()
