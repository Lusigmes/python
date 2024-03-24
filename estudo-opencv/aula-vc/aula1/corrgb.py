import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("entrada.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#imgr,imgg,imgb = cv2.split(img)
imgr = img[:,:,0]
imgg = img[:,:,1]
imgb = img[:,:,2]

img = cv2.merge([imgr,imgg,imgb])

imagens=[imgr,imgg,imgb]

xvalues = np.arange(255)


plt.subplot(1,3,1),plt.imshow(imagens[0],cmap="gray")
plt.subplot(1,3,2),plt.imshow(imagens[1],cmap="gray")
plt.subplot(1,3,3),plt.imshow(imagens[2],cmap="gray")
plt.show()