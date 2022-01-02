# Making imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)

# Preprocessing Input data
# data = pd.read_csv('data.csv')
# X = data.iloc[:, 0]
# Y = data.iloc[:, 1]


# X = [40, 60, 80, 100, 120, 140, 160]
# X = np.array(X, dtype=np.float)
# Y = [29.0, 39.0, 45.2, 53.3, 59.1, 63.5, 71.9]
# Y = np.array(Y, dtype=np.float)

# X = [29.0, 39.0, 45.2, 53.3, 59.1, 63.5, 71.9]
# X = np.array(X, dtype=np.float)
# Y = [40, 60, 80, 100, 120, 140, 160]
# Y = np.array(Y, dtype=np.float)


X = [0.26, 0.32, 0.38, 0.45, 0.50, 0.56, 0.63, 0.71, 0.75]
X = np.array(X, dtype=np.float)
# Y = [190, 185, 180, 175, 170, 165, 160, 155, 150]
Y = [188, 183, 178, 173, 168, 163, 158, 153, 148]
Y = np.array(Y, dtype=np.float)


# plt.scatter(X, Y)
# plt.show()

# Building the model
X_mean = np.mean(X)
Y_mean = np.mean(Y)

num = 0
den = 0
for i in range(len(X)):
    num += (X[i] - X_mean)*(Y[i] - Y_mean)
    den += (X[i] - X_mean)**2
m = num / den
c = Y_mean - m*X_mean

print (m, c)

# Making predictions
Y_pred = m*X + c

plt.scatter(X, Y) # actual
# plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red') # predicted
plt.plot([min(X), max(X)], [max(Y_pred), min(Y_pred)], color='red') # predicted
plt.show()