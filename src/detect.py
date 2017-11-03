import cv2

import sys


def detect(src_img, dst_img):
    casc_file = "./haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(casc_file)
    image = cv2.imread(src_img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.09,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite(dst_img, image)
    return image


if __name__ == "__main__":
    src_image = sys.argv[1]
    dst_image = sys.argv[2]
    detect(src_image, dst_image)
