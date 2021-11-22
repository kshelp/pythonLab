# 람다(lamba) 함수: 익명 함수식
# 형식: lamba <인자> : <인자 활용 수행 코드>
#       lamba <인자> : <인자 활용 수행 코드> (<인자>)
# 1. 이름이 있는 함수를 정의한다.
def exp(x):
    return x**2


# exp(3) 함수를 호출한다.
print(exp(3))  # 9


# 2. 익명 함수를 람다식으로 표현한다.
print((lambda x: x**2)(3))  # 9


# 3. 익명 함수를 변수에 지정하여 이름을 부여한다.
mySquare = lambda x: x**2
print(mySquare(3))  # 9
