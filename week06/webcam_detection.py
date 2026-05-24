import cv2

# 1). Loading file Haarcascade
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print('Can not found file cascade!')
    exit()

cap = cv2.VideoCapture(0)

if not cap.read():
    print('Can not reading the camera')
    exit()

while True:
    res, frame = cap.read()

    if not res:
        print('Not found the camera')
        exit()

    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray_scale,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

    cv2.imshow('Webcam face detection', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()