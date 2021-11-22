file_name = './ch09_str/coffeeShopSales.txt'

f = open(file_name)
for line in f:
    print(line, end='')

f.close()


# 파일에서 읽은 문자열 데이터 처리
f = open(file_name)
header = f.readline()  # 데이터의 첫 번째 줄을 읽음
f.close()

print(header)
# 날짜    에스프레소  아메리카노  카페라테  카푸치노


f = open(file_name)
header = f.readline()
header_list = header.split()  # 첫 줄의 문자열을 분리한 후 리스트로 반환
print(header_list)

for line in f:                # 두 번째 줄부터 반복적으로 처리
    data_list = line.split()
    print(data_list)

f.close()
'''
['날짜', '에스프레소', '아메리카노', '카페라테', '카푸치노']
['10.15', '10', '50', '45', '20']
['10.16', '12', '45', '41', '18']
['10.17', '11', '53', '32', '25']
['10.18', '15', '49', '38', '22']
'''


f = open(file_name)
header = f.readline()
header_list = header.split()

expresso =[]
americano = []
cafelatte = []
cappucino = []

for line in f:
    dataList = line.split()

    expresso.append(int(dataList[1]))
    americano.append(int(dataList[2]))
    cafelatte.append(int(dataList[3]))
    cappucino.append(int(dataList[4]))

f.close()

print("{0}: {1}".format(header_list[1], expresso))
print("{0}: {1}".format(header_list[2], americano))
print("{0}: {1}".format(header_list[3], cafelatte))
print("{0}: {1}".format(header_list[4], cappucino))

total_sum = [sum(expresso), sum(americano), sum(cafelatte), sum(cappucino)]
total_mean = [sum(expresso)/len(expresso), sum(americano)/len(expresso), 
                sum(cafelatte)/len(cafelatte), sum(cappucino)/len(cappucino)]

for k in range(len(total_sum)):
    print('[{0}] 판매량'.format(header_list[k+1]))
    print('- 나흘 전체: {0}, 하루 평균: {1}'.format(total_sum[k], total_mean[k]))