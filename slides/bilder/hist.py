import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("uniformnoise.png", 0)
plt.hist(img.ravel(), 256, [0,256], fc='k', ec='k')
plt.xlim([0, 256])
plt.savefig("uniformnoise_hist.eps", format="eps", bbox_inches='tight')
