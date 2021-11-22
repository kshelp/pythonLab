# 필요없는 문자열 삭제하기
# str.strip([chars])
print("aaaaaPythonaaa".strip('a'))
# Python

test_str = "aaaabbPyathonbbbaa"
temp1 = test_str.strip('a')
print(temp1)
# bbPyathonbbb

print(temp1.strip('b'))
# Pyathon

print(test_str.strip('ab'))
# Pyathon

print(test_str.strip('ba'))
# Pyathon

test_str_multi = "##***!!!##... Python is powerful.!... %%!#...  "
print(test_str_multi.strip('*.#! %'))
# Python is powerful

print(test_str_multi.strip('%!*.# '))
# Python is powerful

print("    Python    ".strip(' '))
# Python

"\n Python  \n\n".strip('\n')
# Python

print("\n This is very \n fast. \n\n".strip())
'''
This is very
 fast.
'''

str_lr = "0000Python is easy to learn.000"
print(str_lr.strip('0'))  # Python is easy to learn.
print(str_lr.lstrip('0')) # Python is easy to learn.000
print(str_lr.rstrip('0')) # 0000Python is easy to learn

coffee_menu = " 에스프레소, 아메리카노, 카페라테, 카푸치노"
coffee_menu_list = coffee_menu.split(',')
print(coffee_menu_list)
# [' 에스프레소', ' 아메리카노', ' 카페라테', ' 카푸치노']

coffee_list = []
for coffe in coffee_menu_list:
    temp = coffe.strip()
    coffee_list.append(temp)

print(coffee_list)
# ['에스프레소', '아메리카노', '카페라테', '카푸치노']