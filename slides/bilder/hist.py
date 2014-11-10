import cv2
import numpy as np
import huffman
from matplotlib import pyplot as plt

sum = 0
bits = 0

img = cv2.imread("moon.jpg", 0)
values = [0 for i in range(0, 256)]
for value in img.ravel():
    values[value] += 1
    sum += 1

for i in range(0, len(values)):
    p = float(values[i])/sum
    c = huffman.h[i]
    bits += values[i]*len(c)
    print str(i) + "," + str(values[i]) + "," + str(p) + "," + c

print float(bits)/sum

#plt.hist(img.ravel(), 256, [0,256], fc='k', ec='k')
#plt.xlim([0, 256])
#plt.savefig("uniformnoise_hist.eps", format="eps", bbox_inches='tight')
