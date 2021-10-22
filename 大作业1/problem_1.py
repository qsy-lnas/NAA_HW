import numpy as np
import matplotlib
from PIL import Image
import math 

sourceim_path = "qrcode_polar.png"
sourceim_type = "png"
targetim_path = "qrcode_carts.png"
targetim_type = "png"


im = Image.open(sourceim_path)
source_image = np.array(im)
image_shape = source_image.shape
target_image = np.zeros(image_shape)
for i in range(np.size(target_image)):
    pass

def rtheta2xy(r, theta):
    x = 2 * math.pi - r * math.sin(theta)
    y = 2 * math.pi + r * math.cos(theta)
    return (x, y)

#x, y \in [0, 4pi] to pixel \in 474, 474(double)
#r != 2pi
def source_xy2pix(x, y):
    x = x / (4 * math.pi) * image_shape[0]
    y = y / (4 * math.pi) * image_shape[1]
    return (x, y)

def target_pix2xy(x, y):
    x = x / image_shape[0] * 2 * math.pi
    y = y / image_shape[1] * 2 * math.pi


print(target_image.shape)