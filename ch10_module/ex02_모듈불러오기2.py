# 모듈을 불러오는 다른 형식
# import 모듈
# from 모듈 import 변수명
# from 모듈 import 함수명
# from 모듈 import 클래스명

from my_area import PI   # 변수
from my_area import square_area  # 함수
from my_area import circle_area  # 함수
# from my_area import *


print('pi=', PI)  
# pi= 3.14

print('square area =', square_area(5))  #  모듈의 함수 이용
print('circle area =', circle_area(2)) 
'''
square area = 25
circle area = 12.56
'''