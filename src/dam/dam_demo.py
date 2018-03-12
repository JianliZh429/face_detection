import cv2
import time
from src import opencv_detector as detector
from src.dam.dam import switcher, close_connection

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    light_status = False
    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            faces = detector.detect(frame)
            if len(faces) > 0 and not light_status:
                result = switcher(True)
                print("Person detected....")
            else:
                result = switcher(False)
                print("No people detected, I turn the light off....")
        else:
            break
        time.sleep(5)

    close_connection()
    cap.release()
    cv2.destroyAllWindows()
