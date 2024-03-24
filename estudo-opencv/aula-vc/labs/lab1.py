import cv2


img = cv2.imread("gamora_nebula.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

faces = detector.detectMultiScale(img, scaleFactor=1.1, 
                                  minNeighbors=5, 
                                  minSize=(30,30), 
                                  flags=cv2.CASCADE_SCALE_IMAGE)

for (x, y, w, h) in faces:
        cv2.rectangle(img=img, pt1=(x,y), pt2=(x+w, y+h), 
                    color=(0, 255, 255), thickness=2, lineType=1 )
            

# cv2.imshow("img_r", img_r)
# cv2.imshow("img_g", img_g)
# cv2.imshow("img_b", img_b)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#nebula 15,104,146 rgb
#gamorra 188,220,147 rgb