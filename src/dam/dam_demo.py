import cv2
import time
from src import opencv_detector as detector
from src.dam.dam import switcher, close_connection

light_status = False


def has_people():
    global light_status
    if not light_status and switcher(True):
        light_status = True
    print("Person detected....")


def no_people():
    global light_status
    if light_status and switcher(False):
        light_status = False
    print("No people detected, I turn the light off....")


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            faces = detector.detect(frame)
            if len(faces) > 0:
                has_people()
            else:
                no_people()
        else:
            break
        time.sleep(5)

    close_connection()
    cap.release()
    cv2.destroyAllWindows()
