# 데이터 연산
import pandas as pd

s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([10,20,30,40,50])
print(s1+s2)
'''
0    11
1    22
2    33
3    44
4    55
dtype: int64
'''

table_data1 = {'A': [1,2,3,4,5],
                'B': [10,20,30,40,50],
                'C': [100,200,300,400,500]}
df1 = pd.DataFrame(table_data1)
print(df1)
'''
   A   B    C
0  1  10  100
1  2  20  200
2  3  30  300
3  4  40  400
4  5  50  500
'''

table_data2 = {'A': [6,7,8],
                'B': [60,70,80],
                'C': [600,700,800]}
df2 = pd.DataFrame(table_data2)
print(df2)
'''
   A   B    C
0  6  60  600
1  7  70  700
2  8  80  800
'''

print(df1+df2)
'''
      A      B       C
0   7.0   70.0   700.0
1   9.0   90.0   900.0
2  11.0  110.0  1100.0
3   NaN    NaN     NaN
4   NaN    NaN     NaN
'''

table_data3 = {'봄': [256.5, 264.3, 215.9, 223.2, 312.8],
                '여름': [770.6, 567.5, 599.8, 387.1, 446.2],
                '가을': [363.5, 231.2, 293.1, 247.7, 381.6],
                '겨울': [193.3, 59.9, 76.9, 169.1, 108.1]}
columns_list = ['봄', '여름', '가을', '겨울']
index_list = ['2012', '2013', '2014', '2015', '2016']

df3 = pd.DataFrame(table_data3, columns=columns_list, index=index_list)
print(df3)
'''
          봄     여름     가을     겨울
2012  256.5  770.6  363.5  193.3
2013  264.3  567.5  231.2   59.9
2014  215.9  599.8  293.1   76.9
2015  223.2  387.1  247.7  169.1
2016  312.8  446.2  381.6  108.1
'''

print(df3.mean())
'''
봄     254.54
여름    554.24
가을    303.42
겨울    121.46
'''

print(df3.mean(axis=1))
'''
2012    395.975
2013    280.725
2014    296.425
2015    256.775
2016    312.175
dtype: float64
'''

print(df3.describe())
'''
                봄          여름          가을          겨울
count    5.000000    5.000000    5.000000    5.000000
mean   254.540000  554.240000  303.420000  121.460000
std     38.628267  148.888895   67.358496   57.845207
min    215.900000  387.100000  231.200000   59.900000
25%    223.200000  446.200000  247.700000   76.900000
50%    256.500000  567.500000  293.100000  108.100000
75%    264.300000  599.800000  363.500000  169.100000
max    312.800000  770.600000  381.600000  193.300000
'''

