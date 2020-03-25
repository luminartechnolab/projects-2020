import os

import cv2

vid = cv2.VideoCapture("./video1.mp4")

fps = vid.get(cv2.CAP_PROP_FPS)
framecount = vid.get(cv2.CAP_PROP_FRAME_COUNT)

print(fps)
print(framecount)

grabbed, frame = vid.read()

count = 0
totalframes = int(framecount*20/100)

while grabbed:

    cv2.imwrite("./videos/frames/frame_%d.png" %
                (len(os.listdir("./videos/frames/")))
                , frame)

    grabbed, frame = vid.read()

vid.release()