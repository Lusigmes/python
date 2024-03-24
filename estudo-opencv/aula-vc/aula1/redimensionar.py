import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

filename = sys.argv[1] # "cat.jpg"
img = cv2.imread(filename) 
imgc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_dst = cv2.imread(filename,0)
# 0 indica que deseja carregar a imagem em ton cinza inves de rgb(1 ou nada)
# print(img_dst.shape) = dimensões da imagem (linhas, colunas)

width = img.shape[1] # comprimento, eixo x
height = img.shape[0] # largura, eixo y

#leitura dos pixels
for comprimento in range(0, width-1):
    for altura in range(0, height-1):
        pixel = imgc.item(altura, comprimento)
        #negativo
        img_dst.itemset(altura, comprimento, 255-pixel)
        
# redimensionamento
new_w = int(imgc.shape[1] * .5)
new_h = int(imgc.shape[0] * .5)
dimensao = (new_w, new_h)
img_resize = cv2.resize(imgc, dimensao, interpolation=cv2.INTER_AREA)
        
# limiarização
ret, img_thresh = cv2.threshold(imgc, 127,255, cv2.THRESH_BINARY)

cv2.imshow("threshold",img_thresh)
cv2.imshow("resized",img_resize)
cv2.imshow("imagem", imgc)
cv2.waitKey(0)
cv2.destroyAllWindows()


