import cv2
import time
import random

start_time = time.time()
videoCaptureObject = cv2.VideoCapture(0)
def take_snapshot():
    number = random.randint(0,100)
    #initializing cv2
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name


def main():
    while(True):
        if ((time.time() - start_time) >= 10):
            name = take_snapshot()
            # upload_file(name)

main()
print("snapshot taken")
videoCaptureObject.release()
cv2.destroyAllWindows()