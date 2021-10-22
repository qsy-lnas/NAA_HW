import numpy as np
import matplotlib
from PIL import Image
import math 


def rtheta2xy(r, theta):
    x = 2 * math.pi + r * math.sin(theta)
    y = 2 * math.pi - r * math.cos(theta)
    if x == 4 * math.pi:
        x -= 0.0001
    elif y == 4 * math.pi:
        y -= 0.0001
    return x, y

def source_xy2pix(x, y, shape):
    '''
    x, y \in [0, 4pi](double) to pixel \in [474, 474](double)
    
    r != 2pi
    --------
    '''
    
    x = x / (4 * math.pi) * shape[0]
    y = y / (4 * math.pi) * shape[1]
    return x, y

def target_pix2xy(x, y, shape):
    '''
    pixel \in [474, 474](int) to x, y \in [0, 2\pi](double)
    
    '''
    x = x / shape[0] * 2 * math.pi
    y = y / shape[1] * 2 * math.pi
    return x, y

sourceim_path = "qr_polar.jpg"
sourceim_type = "jpg"
targetim_path = "qr_carts.jpg"
targetim_type = "jpg"

'''read file'''
im = Image.open(sourceim_path)
source_image = np.array(im)
'''get the 0 channel of source image'''
source_image = source_image[:, :, 0]
image_shape = source_image.shape
#print(image_shape, np.size(source_image))
target_image = np.zeros(image_shape)
for i in range(image_shape[0] * image_shape[1]):
    '''get pix_x, pix_y of this pixel in target figure'''
    pix_y = i // image_shape[1]
    pix_x = i % image_shape[1]
    '''change the coordinate to length of x, y(double)
    r, theta = x, y'''
    x, y = target_pix2xy(pix_x, pix_y, image_shape)
    '''change the r, theta to coordinate of x, y'''
    x, y = rtheta2xy(x, y)
    '''change the x, y to pix_x, pix_y in source_image'''
    x, y = source_xy2pix(x, y, image_shape)
    #if x >= 474 or y >= 474:
    #    print("pix_x = %d, pix_y = %d"%(pix_x, pix_y))
    #    print("x = %f, y = %f"%(x, y))
    if (x % 1 == 0) and (y % 1 == 0):
        '''pixel locate on pixel'''
        target_image[pix_x, pix_y] = \
            source_image[int(x), int(y)]
    else:
        x0 = int(math.floor(x))
        x1 = int(math.ceil(x))
        y0 = int(math.floor(y))
        y1 = int(math.ceil(y))
        if x1 == 474: x1 = 473
        if y1 == 474: y1 = 473
        '''for debugging of 474 outof range'''
        #if x0 >= 474 or x1 >= 474 or y0 >= 474 or y1 == 474:
        #    print("x0 = %d, x1 = %d, y0 = %d, y1 = %d"\
        #        %(x0, x1, y0, y1))
        #    print("pix_x = %d, pix_y = %d, x = %f, y = %f"%\
        #        (pix_x, pix_y, x, y))
        if x % 1 == 0:
            '''single linear interpolation in y'''
            p = (y - y0) * source_image[x0, y1] \
                + (y1 - y) * source_image[x0, y0]
        elif y % 1 == 0:
            '''single linear interpolation in x'''
            p = (x - x0) * source_image[x1, y0] \
                + (x1 - x) * source_image[x0, y0]
        else:
            '''interpolation in x'''
            p0 = (y - y0) * source_image[x0, y1]\
                + (y1 - y) * source_image[x0, y0]
            p1 = (y - y0) * source_image[x1, y1]\
                + (y1 - y) * source_image[x1, y0]
            '''interpolation in y'''
            p = p1 * (x - x0) + p0 * (x1 - x)
        #if pix_x >= 474 or pix_y >= 474:
        #    print("pix_x = %d, pix_y = %d"%(pix_x, pix_y))
        target_image[int(pix_x), int(pix_y)] = p
        '''debug for answer value'''
        if pix_y == 0 and pix_x % 100 == 0:
            print("source_pix = (%f, %f)"%(x, y))
            print("interpoint = (%d, %d, %d, %d)"%(x0, x1, y0, y1))
            print("target_pix = (%d, %d)"%(pix_x, pix_y))
            print("source_value = (%d, %d, %d, %d)"%(source_image[x0, y0], \
                source_image[x0, y1], source_image[x1,y0], source_image[x1, y1]))
            print("target_value = %d"%target_image[pix_x, pix_y])
            print("-----------------------")
        
    
#print(target_image)
#print(type(target_image))
'''map t_i to 0-255(int)'''
result_image = np.zeros(image_shape)
for i in range(image_shape[0] * image_shape[1]):
    x = i // image_shape[1]
    y = i % image_shape[1]
    if target_image[x][y] > 0.5 * 255:
        result_image[x][y] = 1
    else:
        result_image[x][y] = 0
#print(result_image[199: 201, :])
im = Image.fromarray(target_image, 'L')
im.save(targetim_path)
print("Convert successfully")
            

