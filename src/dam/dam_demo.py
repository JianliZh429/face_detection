import cv2

from src import opencv_detector as detector
from src.dam.dam import switcher

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
                switcher(True)
                print("Person detected....")
            else:
                switcher(False)
                print("No people detected, I turn the light off....")
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
