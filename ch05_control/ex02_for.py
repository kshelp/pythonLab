# 반복문의 필요성
a = 0
print(a)

a = a + 1
print(a)

a = a + 1
print(a)

# for 문의 구조
# for <반복 변수> in <반복 범위>
#    <코드 블록>
# 반복 범위 지정
# 리스트 이용
for a in [0,1,2,3,4,5]:  # cf) 자바인 경우, for(변수:배열) 
    print(a)

myFriends = ['James', 'Robert', 'Lisa', 'Mary']
for myFriend in myFriends:
    print(myFriend)
'''
James
Robert
Lisa
Mary
'''

# range() 함수 이용
# 형식: range(start, stop, step)
print(range(0,10,1))        # range(0, 10)
print(list(range(0,10,1)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for a in range(0,10,1):
    print(a)
'''
0
1
2
3
4
5
6
7
8
9
'''

print(list(range(0,10,1)))
print(list(range(0,10)))
print(list(range(10)))
'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

print(list(range(0,20,5)))
print(list(range(-10,0,2)))
print(list(range(3,-10,-3)))
print(list(range(0,-5,1)))
'''
[0, 5, 10, 15]
[-10, -8, -6, -4, -2]
[3, 0, -3, -6, -9]
[]
'''

# 중첩 for문
x_list=['x1','x2']
y_list=['y1','y2']

print("x y")
for x in x_list:
    for y in y_list:
        print(x,y)
'''
x y
x1 y1
x1 y2
x2 y1
x2 y2
'''

# 여러 개의 리스트 다루기
names = ['James', 'Robert', 'Lisa', 'Mary']
scores = [95, 96, 97, 94]

for k in range(len(names)):
    print(names[k], scores[k])
'''
James 95
Robert 96
Lisa 97
Mary 94
'''

for name, score in zip(names, scores):
    print(name, score)
'''
James 95
Robert 96
Lisa 97
Mary 94
'''
