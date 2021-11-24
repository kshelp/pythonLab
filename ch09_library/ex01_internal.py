# 내장 함수
# abs(x): 절대값
# all()
# any()
# chr(i)
print(chr(65))  # A
print(chr(44032)) # 가

# dir은 객체가 자체적으로 가지고 있는 변수와 함수를 보여준다.
print(dir([1,2,3]))  # 리스트 객체
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', 
'__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''

print(dir({'1':'a'})) # 딕셔러니 객체
'''
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', 
'__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'] 
'''

# divmod()은 몫과 나머지를 튜플 형태로 리턴하는 함수이다.
print(divmod(7,3))
# (2, 1)
print(int(7/3))  # 2
print(7%3)       # 1

# enumerate() 함수: 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력을 받아
# 인덱스 값을 포함하는 enumerate 객체로 리턴한다.
i = 0
for name in ['body', 'foo', 'bar']:
    i += 1
    print(i-1, name)
'''
0 body
1 foo
2 bar
'''

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
'''
0 body
1 foo
2 bar
'''

# eval(expression) 함수는 실행 가능한 문자열을 입력으로 받아
# 문자열을 실행한 결과값으로 리턴하는 함수이다.
print("1+2")  # "1+2"
print(eval("1+2"))  # "3"

print('divmod(4,3)')  # "divmod(4,3)"
print(eval('divmod(4,3)'))  # "(1, 1)"


# filter() 함수는 첫번째 인수로 함수이름을, 두번째 인수로 그 함수에 
# 차례로 들어갈 반복 가능한 자료형을 받는다.
def positive(l):
    result = []
    for i in l:
        if i>0:
            result.append(i)
    return result

print(positive([1,-2,-3,4,-5]))
# [1, 4]

def positive1(x):
    return x>0  # True or False

print(list(filter(positive1, [1,-2,-3,4,-5])))
# [1, 4]

print(list(filter(lambda x: x>0, [1,-2,-3,4,-5])))
# [1, 4]


# id(object) 함수는 객체를 입력받아 객체의 고유 주소값을 리턴한다.
a = 3
print(id(3))  # 140736123250528
print(id(a))  # 140736123250528


# map(f, iterable) 함수은 함수(f)와 반복가능한(iterable) 자료형을 입력으로 받는다.
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)
# [2, 4, 6, 8]

def two_times1(x):
    return x*2

print(list(map(two_times1, [1,2,3,4])))
# [2, 4, 6, 8]