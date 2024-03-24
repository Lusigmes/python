
import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

# filename = sys.argv[1]
img = cv2.imread("imagens/cat.jpg")
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

#DIM
w = img.shape[1]
h = img.shape[0]

# MATRIZES DE TRANSFORMAÇÃO

# [ a, b, Tx] - b controla o cisalhamento de x em fator de y
# [ c, d, Ty] - c controla o cisalhamento de y em fator de x
# enquando a e d controram a escala e rotação em X e Y
# T(x,y) - translação de x e y

#rotaciona 45 graus
x_center = w/2
y_center = h/2
m_rotated = cv2.getRotationMatrix2D((x_center,y_center), 45, 1)
# m_rotated = np.float32([[0.86, 0.5, 0], [-0.5, 0.86, 0]])
# print(m_rotaciona)

# scaling x 0.7
m_scaling = np.float32([[1, 0, 0], [0, 0.7, 0]])

# translation(180, 100)
m_translation = np.float32([[1, 0, 180], [0, 1, 100]])

# cisalhamento hotizontal
m_cisalhamentoh = np.float32([[1, 0.5, 0], [0, 1, 0]]) # y em fator do eixo x

# cisalhamento vertical
m_cisalhamentov = np.float32([[1, 0, 0], [0.5, 1, 0]]) # x em fator do eixo y

#computa transformações
img_rotacionada = cv2.warpAffine(img, m_rotated, (w, h))
img_dimensinoada = cv2.warpAffine(img, m_scaling, (w, h))
img_traduzida = cv2.warpAffine(img, m_translation, (w, h))
img_cisalhah = cv2.warpAffine(img, m_cisalhamentoh, (w, h))
img_cisalhav = cv2.warpAffine(img, m_cisalhamentov, (w, h))

# cv2.cvtColor(sourceimg , cv2.COLOR_RGB2BGR)
# cv2.imshow('original',img)
# cv2.imshow('Rotate',img_rotacionada)
# cv2.imshow('Scaling',img_dimensinoada)
# cv2.imshow('Translation',img_traduzida)
# cv2.imshow('cisalhamento hotizontal',img_cisalhah)
# cv2.imshow('cisalhamento vertical',img_cisalhav)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
"""plt.subplot
plt.subplot(221) , plt.imshow(img, cmap="gray")
plt.subplot(222) , plt.imshow(img_rotacionada, cmap="gray")
plt.subplot(223) , plt.imshow(img_dimensinoada, cmap="gray")
plt.subplot(224) , plt.imshow(img_traduzida, cmap="gray")
"""
plt.subplot(221) , plt.imshow(img_cisalhah, cmap="gray")
plt.subplot(222) , plt.imshow(img_cisalhav, cmap="gray")
plt.show()