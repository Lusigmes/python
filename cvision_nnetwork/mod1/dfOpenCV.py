import cv2

imagem = cv2.imread('imagens/pessoas.jpg')

imagem = cv2.resize(imagem,(600, 400))
print(imagem.shape)
imagemGray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

detectar_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

detectados = detectar_face.detectMultiScale(imagemGray, scaleFactor=1.1, minNeighbors=5, minSize=(20,20))

print(detectados)
print(len(detectados))

for x,y,w,h in detectados:
    print(x,y,w,h)
    cv2.rectangle(imagem, (x,y), (x+w,y+h), (35,255,35), 2)

cv2.imshow("img", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()