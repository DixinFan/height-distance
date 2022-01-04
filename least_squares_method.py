import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12.0, 9.0)

# X = [29.0, 39.0, 45.2, 53.3, 59.1, 63.5, 71.9]
# Y = [40, 60, 80, 100, 120, 140, 160]

X = [0.26, 0.32, 0.38, 0.45, 0.50, 0.56, 0.63, 0.71, 0.75]
Y = [190, 185, 180, 175, 170, 165, 160, 155, 150]

X = np.array(X, dtype=np.float)
Y = np.array(Y, dtype=np.float)
X_mean = np.mean(X)
Y_mean = np.mean(Y)

num = 0
den = 0
for i in range(len(X)):
    num += (X[i] - X_mean)*(Y[i] - Y_mean)
    den += (X[i] - X_mean)**2
m = num / den
c = Y_mean - m*X_mean

print(m, c)

Y_pred = m*X + c
plt.scatter(X, Y)
plt.plot([min(X), max(X)], [max(Y_pred), min(Y_pred)], color='red')
plt.show()