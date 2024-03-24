import cv2
import cv_utils

background  = cv2.imread("imagens/bg.jpg")
foreground  = cv2.imread("imagens/fg.jpg")


background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)
foreground = cv2.cvtColor(foreground, cv2.COLOR_BGR2RGB)

imgRed, imgGreen, imgBlue = cv2.split(foreground)

largura = foreground.shape[1]
altura = foreground.shape[0]

# redimensionar o bg
dim =  (largura, altura)
background_ = cv2.resize(background, dim, interpolation=cv2.INTER_AREA)

# threshold
_,background_mask = cv2.threshold(imgGreen, 250, 255, cv2.THRESH_BINARY)

# reaplica a mascara
background_mask = cv2.cvtColor(background_mask, cv2.COLOR_GRAY2BGR)
foreground_mask = cv2.bitwise_not(background_mask)

# combinação de imagens
foreground_ = cv2.bitwise_and(foreground, foreground_mask)
background_ = cv2.bitwise_and(background_, background_mask)



resultado = cv2.add(background_,foreground_)
resultado = cv2.cvtColor(resultado, cv2.COLOR_RGB2BGR)
print(dim)
cv2.imshow("resultado",resultado)
# cv2.imshow("fg",foreground)
cv2.waitKey(0)
cv2.destroyAllWindows()