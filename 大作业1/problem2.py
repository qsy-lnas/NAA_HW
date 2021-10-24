import math
import os

import numpy as np
from tqdm import tqdm

import save_ply

file_path = "sdf.npy"
save_path = "sdf.ply"
save_points_path = "surface_points.npy"
'''the scale of cube'''
scale = 3.0
'''the step of x, y coordinate'''
step = 1e-2
'''the step of trial in z coordinate'''
z_step =5e-3
'''the threshole of sdf in trilinear'''
threshold = 1e-3

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
    #for debugging
    #print("the coordinate of length:", x, y, z)
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
    if x0 == x1:
        p00 = data[x0, y0, z0, 3]
        p01 = data[x0, y0, z1, 3]
        p10 = data[x0, y1, z0, 3]
        p11 = data[x0, y1, z1, 3]
    else:
        p00 = data[x0, y0, z0, 3] * (x1 - x) \
            + data[x1, y0, z0, 3] * (x - x0)
        p01 = data[x0, y0, z1, 3] * (x1 - x) \
            + data[x1, y0, z1, 3] * (x - x0)
        p10 = data[x0, y1, z0, 3] * (x1 - x) \
            + data[x1, y1, z0, 3] * (x - x0)
        p11 = data[x0, y1, z1, 3] * (x1 - x) \
            + data[x1, y1, z1, 3] * (x - x0)
    '''Interpolation in y'''
    if y0 == y1:
        p0 = p00
        p1 = p01
    else:
        p0 = p00 * (y1 - y) + p10 * (y - y0)
        p1 = p01 * (y1 - y) + p11 * (y - y0)
    '''Interpolation in z'''
    if z0 == z1:
        p = p0
    else:
        p = p0 * (z1 - z) + p1 * (z - z0)
    #for debugging
    #if int(x0 + y0 + z0) % 100 == 0:
    #    print(data[x0, y0, z0, 3], data[x0, y0, z1, 3],data[x0, y1, z0, 3],data[x0, y1, z1, 3],"\n",data[x1, y0, z0, 3],data[x1, y0, z1, 3],data[x1, y1, z0, 3],data[x1, y1, z1, 3])
    #    print("the index of coordinate,", x, y, z)
    #    print("the value:", p)
    #    print("----------------------------------")
    #    os.system("pause")
    return p



'''(101, 101, 101, 4)'''
data = np.load(file_path)
'''surface point list'''
sd = []
'''min point in one interval'''
min = float("inf")
min_pos = []
'''x coordinate'''
for i in tqdm(np.arange(scale * -1, scale, step)):
    '''y coordinate'''
    for j in np.arange(scale * -1, scale, step):
        '''z coordinate'''
        for k in np.arange(scale * -1, scale, z_step):
            a = Trilinear(i, j, k, data)
            #print(i, j, k)
            #print(a)
            if abs(a) < threshold and abs(a) < min:
                '''store the min point in this interval'''
                min = abs(a)
                min_pos = [i, j, k]
            elif abs(a) > threshold and abs(a) > min:
                '''append the min point to ply'''
                print(len(sd), min_pos, "a =", a, "min = ", min)
                sd.append(min_pos)
                '''reinit the min'''
                min = float("inf")
                min_pos = []
                
            
sd = np.array(sd)
save_ply.write_ply(save_path, sd)
np.save(save_points_path, np.array(sd))
print("save succeed")




