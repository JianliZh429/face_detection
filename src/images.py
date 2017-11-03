import cv2


def save(filename, image):
    cv2.imwrite(filename, image)
    return image
