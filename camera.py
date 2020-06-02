import cv2
 
cap = cv2.VideoCapture(0)

def Take_Image(img):
    while True:
        ret, frame = cap.read()
        k = cv2.waitKey(1)

        if k == 27:
            break

        elif k == ord(' '):
            cv2.imwrite(img, frame)
            break

        cv2.imshow("capture", frame)

    cap.release()
    cv2.destroyAllWindows()