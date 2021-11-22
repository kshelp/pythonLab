# 변수의 범위: 함수 안에서 정의한 변수는 함수 안에서만 사용할 수 있다.
a = 5   # 전역변수


def func1():
    a = 1  # 지역변수
    print("[func1] 지역 변수 a=", a)


func1()  # [func1] 지역 변수 a= 1
print(a)  # 5


def func4():
    global a
    a = 4   # 전역 변수
    print("[func4] 전역 변수 a=", a)


func4()     # [func4] 전역 변수 a= 4
print(a)    # 5 -> 4
