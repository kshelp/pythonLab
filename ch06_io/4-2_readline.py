# 파일에서 문자열 한 줄씩 읽기
# readline()
f = open("./ch06_io/two_times_table.txt")
line1 = f.readline()  # 한 줄씩 문자열을 읽기
line2 = f.readline()
f.close()
print(line1)
print(line2)
'''
2 x 1 = 2

2 x 2 = 4

'''

f = open("./ch06_io/two_times_table.txt")
line = f.readline()
while line:
    print(line, end="")
    line = f.readline()
f.close()
print(line)
'''
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
'''

# readlines()
# readline()은  파일에서 문자열을 한 줄씩 읽어온다.
# readlines()은 파일 전체의 모든 줄을 읽어서 한 줄씩을 요소로 
# 갖는 리스트 타입으로 반환한다.
f = open("./ch06_io/two_times_table.txt")
lines = f.readlines()
f.close()
print(lines)
# ['2 x 1 = 2\n', '2 x 2 = 4\n', '2 x 3 = 6\n', '2 x 4 = 8\n', '2 x 5 = 10\n']


f = open("./ch06_io/two_times_table.txt")
lines = f.readlines()
f.close()
for line in lines:
    print(line, end="")  # 리스트 항목을 출력(줄 바꿈 안함)
'''
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
'''

f = open('./ch06_io/two_times_table.txt')
for line in f.readlines():
    print(line, end="")
f.close()
'''
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
'''


f = open('./ch06_io/two_times_table.txt')
for line in f:  #  파일 전체를 읽고, 리스트 항목을 line에 할당
    print(line, end="")
f.close()
'''
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
'''
