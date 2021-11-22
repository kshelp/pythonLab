# 유용한 내장 함수
# 형 변환 함수
# 정수형으로 변환
print([int(0.123), int(3.5123456), int(-1.312346)])
# [0, 3, -1]

# 실수형으로 변환
print([float(0), float(123), float(-567)])
# [0.0, 123.0, -567.0]

# 문자형으로 변환
print([str(123), str(45678), str(-87)])
# ['123', '45678', '-87']

# 리스트, 튜플, 세트형으로 변환
list_data = ['abc', 1, 2, 'def']
tuple_data = ('abc', 1, 2, 'def')
set_data = {'abc', 1, 2, 'def'}

print([type(list_data), type(tuple_data), type(set_data)])
# [<class 'list'>, <class 'tuple'>, <class 'set'>]

print("리스트로 변환: ", list(tuple_data), list(set_data))
# 리스트로 변환:  ['abc', 1, 2, 'def'] [1, 2, 'def', 'abc']

print("튜플로 변환: ", tuple(list_data), tuple(set_data))
# 튜플로 변환:  ('abc', 1, 2, 'def') ('def', 1, 2, 'abc')

print("세트로 변환: ", set(list_data), set(tuple_data))
# 세트로 변환:  {'abc', 1, 2, 'def'} {'abc', 1, 2, 'def'}

# bool 함수
# 숫자를 인자로 bool 함수 호출
print(bool(0))  # False
print(bool(1))  # True
print(bool(-10))    # True

# 문자열을 인자로 bool 함수 호출
print(bool('a'))    # True
print(bool(' '))    # True
print(bool(''))     # False
print(bool(None))   # False

# 리스트, 튜플, 세트를 인자로 bool 함수 호출
myFirends = []
print(bool(myFirends))  # False

myFirends = ['James', 'Robert']
print(bool(myFirends))  # True

myNum = ()
print(bool(myNum))  # False

mySetA = {}
print(bool(mySetA)) # False

# bool 함수의 활용
def print_name(name):
    if bool(name):
        print("입력된 이름:", name)
    else:
        print("입력된 이름이 없습니다.")

print_name("James") # 입력된 이름: James
print_name("")      # 입력된 이름이 없습니다.

# 최솟값과 최댓값을 구하는 함수
myNum = [10, 5, 12, 0, 3.5, 99.5, 42]
print([min(myNum), max(myNum)])
# [0, 99.5]

myStr = 'zxyabc'
print([min(myStr), max(myStr)])
# ['a', 'z']

myNum = ["Abc", "abc", "bcd", "efg"]
print([min(myNum), max(myNum)])
# ['Abc', 'efg']

# 절대값과 전체 합을 구하는 함수
print([abs(10), abs(-10)])  # [10, 10]
sumList = [1,2,3,4,5,6,7,8,9,10]
print(sum(sumList)) # 55

# 항목의 갯수를 구하는 함수
print(len("ab cd"))  # 5
print(len([1, 2, 3, 4, 5, 6, 7, 8]))    # 8
print(len({1:"Thomas", 2:"Edward", 3:"Henry"})) # 3

# 내장 함수의 활용
scores = [90,80,95,85]

score_sum = 0
subject_num = 0
for score in scores:
    score_sum = score_sum + score
    subject_num = subject_num + 1  # 과목수 계산

average = score_sum / subject_num
print("총점:{0}, 평균:{1}".format(score_sum, average))
# 총점:350, 평균:87.5

scores = [90,80,95,85]
print("총점:{0}, 평균{1}".format(sum(scores), sum(scores)/len(scores)))
# 총점:350, 평균87.5
print("최하 점수: {0}, 최고 점수:{1}".format(min(scores), max(scores)))
# 최하 점수: 80, 최고 점수:95


print("\n*** 재귀적 함수 호출 ***")
def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)


# 3! = 3x2!
print(factorial(4))  # 24


# Tower of Hanoi
def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
        print(startPeg, "번 기둥의", ndisks, "번 원반을", endPeg, "번 기둥에 옮깁니다.")
        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)

hanoi(ndisks=5)