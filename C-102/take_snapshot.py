import cv2

def snapshot():
    capture = cv2.VideoCapture(0)
    result = True

    while (result):
        ret,frame = capture.read()
        print(ret)
        cv2.imwrite("test.jpg",frame)
        result = False

    capture.release()
    cv2.destroyAllWindows()

snapshot()    