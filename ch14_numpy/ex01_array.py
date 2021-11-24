# 시퀀스 데이터로부터 배열 생성
import numpy as np

data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1)
print(a1)  # [0 1 2 3 4 5]
print(a1.dtype)  # int32

data2 = [0, 1, 5, 4, 12, 0.5]
a2 = np.array(data2)
print(a2)  # [ 0.   1.   5.   4.  12.   0.5]
print(a2.dtype)  # float64

print(np.array([0.5, 2, 0.01, 8]))  # [0.5  2.   0.01 8.  ]

print(np.array([[1,2,3],[4,5,6],[7,8,9]]))
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
