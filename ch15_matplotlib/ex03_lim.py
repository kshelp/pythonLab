# 그래프의 출력 범위 지정하기
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 100)  # [-4, 4] 범위에서 100의 값 생성
y1 = x**3
y2 = 10*x**2 -2

plt.plot(x, y1, x, y2)
#plt.show()

plt.figure()
plt.plot(x, y1, x, y2)
plt.xlim(-1, 1)
plt.ylim(-3, 3)
plt.show()