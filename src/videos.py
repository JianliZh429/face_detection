import cv2


class VideoWriter:
    def __init__(self, fps=40, frame_size=(1920, 1080)):
        # fourcc = cv2.VideoWriter_fourcc(*'X264')
        self.out = cv2.VideoWriter('output.avi', -1, 30, (1280, 720))

    def save(self, frame):
        self.out.write(frame)

    def __exit__(self, exc_type, exc_value, traceback):
        self.out.release()


def build_filename(count=0):
    dynamic_part = "{0:08}".format(count)
    return '{}_{}.jpg'.format('me', dynamic_part)


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    # Define the codec and create VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter('output.avi', fourcc, 20.0)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # frame = cv2.flip(frame, 0)

            # write the flipped frame
            # frame = cv2.resize(frame, (640, 480))
            # out.write(frame)
            filename = build_filename(count)
            cv2.imwrite(filename, frame)

            count += 1
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    # out.release()
    cv2.destroyAllWindows()
