# 행렬 연산
import numpy as np

A = np.array([0,1,2,3]).reshape(2,2)
print(A)
'''
[[0 1]
 [2 3]]
'''

B = np.array([3,2,0,1]).reshape(2,2)
print(B)
'''
[[3 2]
 [0 1]]
'''

# 행렬곱(A x B)
print(A.dot(B))
'''
[[0 1]
 [6 7]]
PS D:\d
'''

print(np.dot(A,B))
'''
[[0 1]
 [6 7]]
'''

# A의 전치행렬
print(np.transpose(A))
'''
[[0 2]
 [1 3]]
'''

print(A.transpose())
'''
[[0 2]
 [1 3]]
'''

# 행렬 A의 역행렬
# 역행렬의 공식
# A = [[a b]
#      [c d]] 
#  1/(ad-db) A^t       
print(np.linalg.inv(A))
'''
[[-1.5  0.5]
 [ 1.   0. ]]
'''

print(np.linalg.det(A))  # -2.0




