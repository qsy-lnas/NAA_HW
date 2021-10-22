from PIL import Image
import numpy as np
import math

sourceim_path = "qr_polar.jpg"
testim_path = "qr_test.jpg"
im = Image.open(sourceim_path)
source_image = np.array(im)
print(source_image[4, :, 0])
#im = Image.fromarray(source_image[:, :, 0], 'L')
#im.save(testim_path)