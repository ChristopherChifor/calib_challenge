import numpy as np
import cv2


def process_frame(img):
    print(img.shape)

if name == '__main__':

    cap = cv2.VideoCapture('5.hevc')

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            process_frame(frame)
        else:
            break
