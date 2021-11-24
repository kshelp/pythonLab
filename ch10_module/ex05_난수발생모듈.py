# 난수 발생 모듈
# import random
# random.random모듈함수()
import random

print(random.random())   # 0~1사이의 임의의 실수값을 생성한다.
# 0.5514094257160855

dice1 = random.randint(1,6)  # 1~6사이의 임의의 정수값
dice2 = random.randint(1,6)  # 1~6사이의 임의의 정수값
print('주사위 두 개의 숫자: {0}, {1}'.format(dice1, dice2))
# 주사위 두 개의 숫자: 4, 5

print(random.randrange(0,11,2))  # 0~10사이의 임의의 짝수

num1 = random.randrange(1,10,2)  # 1~9사이의 임의의 홀수
num2 = random.randrange(0,100,10) # 0~99사이의 10의 배수
print('num1: {0}, num2: {1}'.format(num1, num2))
# num1: 1, num2: 90


menu = ['비빔밥', '된장찌개', '볶음밥', '불고기', '스파게티', '피자', '탕수육']
print(random.choice(menu))
# 불고기

print(random.sample([1,2,3,4,5], 2))  # 모집단에서 두 개의 인자 선택
# [1, 3]