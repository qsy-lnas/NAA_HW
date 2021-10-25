import numpy as np

file_path = "surface_points_1.npy"
#file_path = "surface_points_1e-2.npy"
#file_path = "result.npy"
'''(len, 3)'''
data = np.load(file_path)
epsilon = 1e-10
lowerbound = 1e-3
higherbound = 1e3

data[data == 0] = epsilon
x2, y2, z2 = data[:, 0] ** 2, data[:, 1] ** 2, data[:, 2] ** 2
x2z3 = x2 * z2 * data[:, 2]
y2z3 = y2 * z2 * data[:, 2]
x2y2z23 = np.power(2 * x2 + y2 + z2 - 1, 3)

'''check the y2z3 < lowerbound'''
del_index = np.abs(y2z3) < lowerbound
x2z3 = x2z3[~del_index]
y2z3 = y2z3[~del_index]
x2y2z23 = x2y2z23[~del_index]

y = -(x2y2z23 / y2z3)
x = (x2z3 / y2z3) #not x2 y2 for not processed
#print(y.shape, x.shape)
del_x = (np.abs(x) > higherbound)
del_y = (np.abs(y) > higherbound)
#print(del_x.shape, del_y.shape)
y = y[~np.bitwise_or(del_x, del_y)]
x = x[~np.bitwise_or(del_x, del_y)]

""" for i in range(len(data)):
    if i >= len(data):
        break
    for j in range(3):
        if abs(data[i, j]) < 1e-4: 
            #print("delete:", data[i])
            data = np.delete(data, i, axis = 0)
            i -= 1
            break

y = -1 * (2 * data[:, 0] ** 2 + data[:, 1] ** 2 + data[:, 2] ** 2 - 1) ** 3 \
    / (data[:, 1] ** 2 * data[:, 2] ** 3)
x = (data[:, 0] ** 2) / (data[:, 1] ** 2)

for i in range(len(x)):
    if i >= len(x):
        break
    if abs(x[i]) > 1e4 or abs(y[i]) > 1e4:
        x = np.delete(x, i)
        y = np.delete(y, i)
        i -= 1 """

x_mean = np.mean(x)
y_mean = np.mean(y)
xy_mean = np.mean(x * y)
x2_mean = np.mean(x ** 2)

a = (xy_mean - x_mean * y_mean) / (x2_mean - x_mean ** 2)
b = y_mean - a * x_mean

print("a = %f, b = %f"%(a ,b))