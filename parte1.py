# -*- coding: utf-8 -*-

import numpy as np
from scipy import ndimage
from scipy import misc
from PIL import Image

#x = [] #crea arreglo vacio
im = Image.open('1.jpg').convert('L')
x = np.asarray(im, dtype=np.uint8) #no se que hace esto, prueba
y = np.reshape(x,43621)
print x