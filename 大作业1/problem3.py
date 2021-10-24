import numpy as np

file_path = "surface_points_1e-2.npy"
'''(len, 4)'''
data = np.load(file_path)
y = -(2 * data[:, 0] ** 2 + data[:, 1] ** 2 + data[:, 2] ** 2 - 1) ** 3 \
    / (data[:, 1] ** 2 * data[:, 2] ** 3)
x = data[:, 0] ** 2 / data[:, 1] ** 2
x_mean = np.mean(x)
y_mean = np.mean(y)
xy_mean = np.mean(x * y)
x2_mean = np.mean(x ** 2)

a = (xy_mean - x_mean * y_mean) / (x2_mean - x_mean ** 2)
b = y_mean - k * x_mean

print("a = %f, b = %f"%(a ,b))