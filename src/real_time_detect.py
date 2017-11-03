import logging as log

import cv2

import images
import opencv_detector as detector

log.basicConfig(filename='face_detect.log', level=log.INFO)


def _draw_rectangle(faces, frame):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame


def _build_filename(prefix, count):
    dynamic_part = '{0:08}.jpg'.format(count)
    filename = '{}_{}'.format(prefix, dynamic_part)
    return filename


def detect(video_file=None, save_image=False, prefix='detected', quiet=False):
    if video_file is None or len(video_file) < 1:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(video_file[0])

    count = 0
    video_writer = None

    while cap.isOpened():
        ret, image = cap.read()
        # if ret is True:
        # if video_writer is None:
        #     video_writer = VideoWriter(fps=30, frame_size=(1280, 720))

        filename = _build_filename(prefix, count)

        faces = detector.detect(image)
        log.info("{} detected faces: {}".format(filename, len(faces)))

        image = _draw_rectangle(faces, image)

        # video_writer.save(image)

        if save_image:
            images.save(filename, image)

        count += 1
        if not quiet:
            cv2.imshow('detected', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                # else:
                #     break

    cap.release()
    if not quiet:
        cv2.destroyAllWindows()
