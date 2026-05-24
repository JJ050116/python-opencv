import cv2

cap = cv2.VideoCapture(0)

if not cap.read():
    print('Cannot open the camera')

while True:
    res, frame = cap.read()

    if not res:
        print('Canot receive frame exiting.....')
        break

    cv2.imshow('My camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()