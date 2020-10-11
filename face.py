import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("photo.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(img,scaleFactor=1.05,minNeighbors=5)
print(faces)
print(type(faces))
for x,y,w,h in faces:
    image=cv2.rectangle(gray_img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("img",image)
cv2.waitKey(2000)
cv2.destroyAllWindows()