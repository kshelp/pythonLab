# 문자열 분리하기
# str.split([sep])

coffee_menu_str = "에스프레소,아메리카노,카페라테,카푸치노"
print(coffee_menu_str.split(','))
# ['에스프레소', '아메리카노', '카페라테', '카푸치노']

"에스프레소,아메리카노,카페라테,카푸치노".split(',')

print("에스프레소 아메리카노 카페라테 카푸치노".split(' '))
['에스프레소', '아메리카노', '카페라테', '카푸치노']

print("에스프레소 \n\n 아메리카노 \n 카페라테 카푸치노 \n\n".split())
# ['에스프레소', 'v아메리카노', '카페라테', '카푸치노']

print("에스프레소 아메리카노 카페라테 카푸치노".split(maxsplit=2))

phone_number = "+82-01-2345-6789"
split_num = phone_number.split("-",1)
print(split_num)
# ['+82', '01-2345-6789']