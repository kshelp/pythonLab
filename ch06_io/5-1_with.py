# with 문을 활용해 파일 읽고 쓰기
# with 문의 구조
f = open('./ch06_io/myFile.txt', 'w')
f.write('File write/read test.')
f.close()

# with 문의 활용
with open('./ch06_io/myFile2.txt', 'w') as f:
    f.write('File read/write test2: line1\n')
    f.write('File read/write test2: line2\n')
    f.write('File read/write test2: line3\n')

with open('./ch06_io/myFile2.txt') as f:
    file_string = f.read()
    print(file_string)
'''
File read/write test2: line1
File read/write test2: line2
File read/write test2: line3
'''

with open('./ch06_io/myFile3.txt', 'w') as f:
    for num in range(1,6):
        format_string = "3x{0}={1}\n".format(num,3*num)
        f.write(format_string)


with open('./ch06_io/myFile3.txt', 'r') as f:
    for line in f:  # f.readlines()와 같다.
         print(line, end="")
'''
3x1=3
3x2=6
3x3=9
3x4=12
3x5=15
'''

# with 문의 활용
with open('./ch06_io/myFile4.txt', 'w', encoding='utf-8') as f:
    f.write('한글1\n')
    f.write('한글2\n')
    f.write('한글3\n')