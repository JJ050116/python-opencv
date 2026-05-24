# as it's means use the new name of library or module
import cv2 as opencv

cap = opencv.VideoCapture('video/meme2.mp4')

while cap.isOpened():
    res, frame = cap.read()

    if not res:
        print('Not found the video')
        break

    opencv.imshow('Output', frame)

    # 1 it's means customize press button "q" for exit....
    if opencv.waitKey(1) == ord('q'):
        break

# cv2.waitKey(0) = 0 it's means press any button for....

# it's means show output the image capture from video
cap.release()
opencv.destroyAllWindows()