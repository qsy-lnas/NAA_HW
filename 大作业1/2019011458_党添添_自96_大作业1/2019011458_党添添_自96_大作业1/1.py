import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.stats import mode
import cv2


data = cv2.imread('qr-polar.png',0)
# data = cv2.imread('321.png',0)

center_x = data.shape[0]/2
center_y = data.shape[1]/2 #这是极坐标图的原点坐标


def result_trans_polar(x,y):
    theta = 2*np.pi*x/center_y
    ori_y = center_x+y*np.cos(theta)
    #ori_y = data.shape[1] - (center_y-x*np.sin(theta))
    ori_x = center_y-y*np.sin(theta)
    return float(ori_x),float(ori_y)

def shuangxianchazhi(result_x,result_y,polar_data):

    ori_x,ori_y = result_trans_polar(result_x,result_y)
    u = int(ori_x)
    v = int(ori_y)
    G_x_v = (ori_x - u)*polar_data[u+1][v] - (ori_x- u - 1)*polar_data[u][v]
    G_x_v_add_1 =(ori_x - u)*polar_data[u+1][v+1] - polar_data[u][v+1]*(ori_x - u- 1)

    G_x_y = (v+1-ori_y)*G_x_v+(ori_y-v)*G_x_v_add_1

    result = G_x_y
    return result
result_img = np.zeros((int(data.shape[0]/2),int(data.shape[1]/2)))

for i in range(int(data.shape[0]/2)):
    for j in range(int(data.shape[1]/2)):
        result_img[i][j] = shuangxianchazhi(i,j,data)

cv2.imwrite("result.png",result_img)