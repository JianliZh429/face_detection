import argparse
import logging as log

import cv2

log.basicConfig(filename='face_detect.log', level=log.INFO)


def _draw_rectangle(faces, frame):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame


def _detect_faces(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    return faces


def _get_face_cascade():
    casc_file = "./haarcascade_frontalface_default.xml"
    return cv2.CascadeClassifier(casc_file)


def _save_image(filename, image):
    cv2.imwrite(filename, image)
    return image


def detect(video_file=None, prefix='detected', quiet=False):
    if video_file is None or len(video_file) < 1:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(video_file[0])

    count = 0
    face_cascade = _get_face_cascade()
    while (cap.isOpened()):
        ret, image = cap.read()
        dynamic_part = '{0:08}.jpg'.format(count)
        filename = '{}_{}'.format(prefix, dynamic_part)
        faces = _detect_faces(image, face_cascade)
        log.info("{} detected faces: {}".format(filename, len(faces)))
        image = _draw_rectangle(faces, image)
        _save_image(filename, image)

        if not quiet:
            cv2.imshow(filename, image)
        count += 1

    cap.release()

    if not quiet:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('video_file', nargs='*')
    parser.add_argument('-p', '--prefix', help='prefix of detected output image files')
    parser.add_argument('-q', '--quiet', action='store_true', help='if set, will not show real time result window')
    argv = parser.parse_args()
    print argv
    detect(video_file=argv.video_file, prefix=argv.prefix, quiet=argv.quiet)
