import cv2
import time
video=cv2.VideoCapture(0)
while(True):

    check, frame =video.read()
    
    print(frame)
    # great work.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    cv2.imshow("capturing",gray)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv2.DestroyAllWindows

#doing necessary changes in the code🥱



