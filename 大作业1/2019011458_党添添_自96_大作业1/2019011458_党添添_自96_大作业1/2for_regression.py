import  random
import numpy as np
sdf=np.load('sdf.npy',encoding = "latin1")  #加载文件
print(sdf.shape)
N = 100000000
x = 0
y = 0
z = 0
random.seed(1245)
def find_n(value):
    """
    找到对应的n
    """
    n = int((value+3)/0.06)
    return n

def randomlist(num):
    ls = []
    for i in range(num):
        temp = random.uniform(-3,3)
        ls.append(temp)

    return ls

x_list = randomlist(N)
y_list = randomlist(N)
z_list = randomlist(N)

def sanxianxingchazhi(des_x,des_y,des_z,src_sdf):
    """
    针对非端点的插值
    """
    n_x = find_n(des_x)
    x_n = -3.0 + n_x*0.06
    n_y = find_n(des_y)
    y_n = -3.0 + n_y*0.06
    n_z = find_n(des_z)
    z_n = -3.0 + n_z *0.06

    #先对x插值
    h_n_n_x = (x- x_n)/(0.06) *(src_sdf[n_x+1][n_y][n_z][-1] - src_sdf[n_x][n_y][n_z][-1]) + src_sdf[n_x][n_y][n_z][-1]
    h_nadd1_n_x = (x- x_n)/(0.06) *(src_sdf[n_x+1][n_y+1][n_z][-1] - src_sdf[n_x][n_y+1][n_z][-1]) + src_sdf[n_x][n_y+1][n_z][-1]
    h_n_nadd1_x = (x- x_n)/(0.06) *(src_sdf[n_x+1][n_y][n_z+1][-1] - src_sdf[n_x][n_y][n_z+1][-1]) + src_sdf[n_x][n_y][n_z+1][-1]
    h_nadd1_nadd1_x = (x- x_n)/(0.06) *(src_sdf[n_x+1][n_y+1][n_z+1][-1] - src_sdf[n_x][n_y+1][n_z+1][-1]) + src_sdf[n_x][n_y+1][n_z+1][-1]

    #再对y插值

    g_n_x_y = (y-y_n)/(0.06)*(h_nadd1_n_x-h_n_n_x)+h_n_n_x
    g_nadd1_x_y = (y-y_n)/(0.06)*(h_nadd1_nadd1_x-h_n_nadd1_x)+h_n_nadd1_x

    #再对z插值
    w_z = (z-z_n)/(0.06)*(g_nadd1_x_y-g_n_x_y)+g_n_x_y

    return w_z


f = []
for idx in range(N):
    x = x_list[idx]
    y = y_list[idx]
    z = z_list[idx]
    f_x_y_z = sanxianxingchazhi(x,y,z,sdf)
    f.append(f_x_y_z)

des = []
for idx,inst in enumerate(f):
    if abs(inst)<0.001:
        temp = []
        temp.append(round(x_list[idx],6))
        temp.append(round(y_list[idx],6))
        temp.append(round(z_list[idx],6))
        des.append(temp)

# doc = open('1000000.txt', 'a')  #打开一个存储文件，并依次写入
# print(des, file=doc)

ply_header = '''ply
        		format ascii 1.0
        		element vertex %(vert_num)d
        		property float x
        		property float y
        		property float z
        		property uchar red
        		property uchar green
        		property uchar blue
        		end_header
        		\n
        		'''

with open("hzc.txt","w") as file:

    file.write(ply_header % dict(vert_num = len(des)))
    file.write('\n')
    file.write('\n')
    for idx,inst in enumerate(des):
        file.write(str(inst[0])+' '+str(inst[1])+' '+str(inst[2])+' '+'255'+' '+'255'+' '+'255')
        file.write('\n')


