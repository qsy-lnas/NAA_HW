import numpy as np

file_path = "surface_points_1e-2.npy"
'''(len, 3)'''
data = np.load(file_path)

""" for i in range(len(data)):
    for j in range(3):
        if abs(data[i, j]) < 1e-1:
            print("delete:", data[i])
            np.delete(data, i)
            break """

y = -1 * (2 * data[:, 0] ** 2 + data[:, 1] ** 2 + data[:, 2] ** 2 - 1) ** 3 \
    / (data[:, 1] ** 2 * data[:, 2] ** 3)
x = (data[:, 0] ** 2) / (data[:, 1] ** 2)

for i in range(len(x)):
    if abs(x[i]) > 1e5 or abs(y[i]) > 3:
        np.delete(x, i)
        np.delete(y, i)

x_mean = np.mean(x)
y_mean = np.mean(y)
xy_mean = np.mean(x * y)
x2_mean = np.mean(x ** 2)

a = (xy_mean - x_mean * y_mean) / (x2_mean - x_mean ** 2)
b = y_mean - a * x_mean

print("a = %f, b = %f"%(a ,b))