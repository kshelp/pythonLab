#-*- coding: utf-8 -*-
def gugudan(n):
    # 이 위치에 코드를 작성한다.
    result = []
    i = 1
    while i < 10:
        result.append(i*n)
        i += 1
    return result

print(gugudan(2))
print(gugudan(3))
print(gugudan(4))
'''
[2, 4, 6, 8, 10, 12, 14, 16, 18]
[3, 6, 9, 12, 15, 18, 21, 24, 27]
[4, 8, 12, 16, 20, 24, 28, 32, 36]
'''