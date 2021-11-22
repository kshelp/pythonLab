# Q5 아래와 같이 총 10줄로 이루어진 sample.txt 파일이 있다.
# sample.txt 파일의 숫자값을 모두 읽어 총합과 평균값을 구한 후
# 평균값을 result.txt라는 파일에 쓰는 프로그램을 작성해 보자.
f = open("./ch06_io/sample.txt")
lines = f.readlines()  # sample.txt를 줄 단위로 모두 읽는다.
f.close()

total = 0
for line in lines:
    score = int(line)  # 줄에 적힌 점수를 숫자형으로 변환한다.
    total += score
average = total / len(lines)
print(type(average))    # <class 'float'>

f = open("./ch06_io/result.txt", 'w')
#f.write(average)  # write() argument must be str, not float
f.write(str(average))
f.close()
