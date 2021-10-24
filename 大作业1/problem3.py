import numpy as np

file_path = "surface_points_1e-2.npy"
'''(len, 4)'''
data = np.load(file_path)
y = -(2 * data[:, 0] ** 2 + data[:, 1] ** 2, data[:, 2] ** 2 - 1) ** 3 \
    / (data[:, 1] ** 2 * data[:, 2] ** 3)
x = data[:, 0] ** 2 / data[:, 1] ** 2

for i in range(data.shape[0]):

print(data.shape)