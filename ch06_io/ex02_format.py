# 형식 지정 출력
# 나머지 연산자(%)를 이용한 형식 및 위치 지정
# 형식: print("%type" %data)
#       print("%type %type" %(data1, data2))

name = "광재"
print("%s는 나의 친구입니다." % name)
# 광재는 나의 친구입니다.

r = 3
PI = 3.141592
print("반지름: %d, 원주율: %f" %(r, PI))
# 반지름: 3, 원주율: 3.141592


# 형식 지정 문자열에서 출력 위치 지정
# 형식: print("{0} {1} {2}...{n}".format(data_0, data_1,...data_n))
animal_0 = "cat"
animal_1 = "dog"
animal_2 = "fox"
print("Animal: {0}".format(animal_0))  # Animal: cat
print("Aminal: {0},{1},{2}".format(animal_0,animal_1,animal_2))
# Aminal: cat,dog,fox
print("Animal: {},{},{}".format(animal_0,animal_1,animal_2))
# Animal: cat,dog,fox

name = "Thomas"
age = 10
a = 0.123456789
fmt_string = "String: {0}, Integer Number: {1}, Floating Number: {2}"
print(fmt_string.format(name,age,a))
# String: Thomas, Integer Number: 10, Floating Number: 0.123456789


# 형식 지정 문자열에서 숫자 출력 형식 지정
a = 0.1234567890123456789
print("{0:.2f}, {0:.5f}".format(a))
# 0.12, 0.12346
