from my_module1 import *
from my_module2 import *

func1()
func2()
func3()
'''
func1 in my_module1
func2 in my_module2
func3 in my_module2
'''

# 모듈명을 별명으로 선언
# from 모듈명 import 변수명 as 별명
# from 모듈명 import 함수명 as 별명
# from 모듈명 import 클래스명 as 별명
import my_area as area

print('pi=', area.PI)  # pi= 3.14
print('square area=', area.square_area(5))  # square area= 25
print('circle area=', area.circle_area(2))  # circle area= 12.56

from my_area import PI as pi
from my_area import square_area as square
from my_area import circle_area as circle

print('pi=',pi)
print('square area=', square(5))
print('circle area=', circle(2))
'''
pi= 3.14
square area= 25
circle area= 12.56
'''