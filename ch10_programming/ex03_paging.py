#-*- coding: utf-8 -*-
# 게시판 페이징하기
def getTotalPage(m, n):
    # 이 위치에 코드를 작성한다.
    if m%n == 0:
        return m//n
    else:
        return m//n + 1

print(5/10)    # /는 나누기하여 실수값을 반환한다.
print(11//10)  # // 몫을 산출하여 정수값을 반환한다.
print(5%10)    # %는 나머지 구하여 정수값을 반환한다.

print(getTotalPage(5,10)) # 1    
print(getTotalPage(15,10)) # 2
print(getTotalPage(30,10)) # 3
print(getTotalPage(31,10)) # 4