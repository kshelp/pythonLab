# 선 그래프
import matplotlib.pyplot as plt
import numpy as np

data1 = [10, 14, 19, 20, 25]

plt.plot(data1)
plt.show()


x = np.arange(-4.5, 5, 0.5)
y = 2*x**2     # y = 2x^2
print([x, y])
'''
[array([-4.5, -4. , -3.5, -3. , -2.5, -2. , -1.5, -1. , -0.5,  0. ,  0.5,
        1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5]), array([40.5, 32. , 24.5, 18. 
, 12.5,  8. ,  4.5,  2. ,  0.5,  0. ,  0.5,
        2. ,  4.5,  8. , 12.5, 18. , 24.5, 32. , 40.5])]
'''
plt.plot(x, y)
plt.show()

