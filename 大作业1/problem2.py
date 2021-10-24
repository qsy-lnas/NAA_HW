import numpy as np
import math
from 

file_path = "sdf.npy"
scale = 3

def xyz2index(x, y, z):
    '''
    Input: (x, y, z), the length of coordinate in cube
    Return: the index of x, y, z in data\\
    Scale (0, 100)(double)
    '''
    x = x / 3 * 50 + 50
    y = y / 3 * 50 + 50
    z = z / 3 * 50 + 50
    return x, y, z

def Trilinear(x, y, z, data):
    '''
    Input: (x, y, z), the length of coordinate in cube
    Return: the Trilinear interpolation value of this point
    '''
    x, y, z = xyz2index(x, y, z)
    '''calculate the nearest int point'''
    x0 = math.floor(x)
    x1 = math.ceil(x)
    y0 = math.floor(y)
    y1 = math.ceil(y)
    z0 = math.floor(z)
    z1 = math.ceil(z)
    '''Trilinear interpolation'''
    '''Interpolation in x'''
    p00 = data[x0, y0, z0, 3] * (x1 - x) \
        + data[x1, y0, z0, 3] * (x - x0)
    p01 = data[x0, y0, z1, 3] * (x1 - x) \
        + data[x1, y0, z1, 3] * (x - x0)
    p10 = data[x0, y1, z0, 3] * (x1 - x) \
        + data[x1, y1, z0, 3] * (x - x0)
    p11 = data[x0, y1, z1, 3] * (x1 - x) \
        + data[x1, y1, z1, 3] * (x - x0)
    '''Interpolation in y'''
    p0 = p00 * (y1 - y) + p10 * (y - y0)
    p1 = p01 * (y1 - y) + p11 * (y - y0)
    '''Interpolation in z'''
    p = p0 * (z1 - z) + p1 * (z - z0)
    return p



'''(101, 101, 101, 4)'''
data = np.load(file_path)
print(data.shape, type(data))
print(data[100, 100, 100, :])
