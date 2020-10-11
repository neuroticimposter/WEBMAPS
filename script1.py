import cv2
import glob
images=glob.glob("*.jpg")

# print(type(img))
# print(img)
# print(img.shape)
# cv2.imshow("image",img)
# cv2.waitKey(2000)
for image in images:
    img= cv2.imread(image,0)
    re =cv2.resize(img,(100,100))
    cv2.imshow("image",re)
    cv2.waitKey(2000)
    cv2.imwrite("resized"+image,re)
   
    cv2.destroyAllWindows()