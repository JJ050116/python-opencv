import cv2

# 1) Loading file Haar Cascade
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml' 
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print('Loading file Haarcascade fail!')
    exit()

# 2) Load image
# img = cv2.imread('imgs/erling.png')
# img = cv2.imread('imgs/neymarjr.webp')
# img = cv2.imread('imgs/albon.png')
img = cv2.imread('imgs/team.webp')

if img is None:
    print('Image not found!')
    exit()

# 3) Convert RBG to GrayScale
gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4) Face detection
# .detecMutiScale() = detection object
# If being close to the camera => Big face
# If the object too far from the camera => Small face
faces = face_cascade.detectMultiScale(
    gray_scale, # Standrad image convert to grayscale
    scaleFactor=1.1, # Scan face to reduce the size (reduce 10%)
    minNeighbors=5, # Should believe this area to real face (5 round)
    minSize=(30, 30) # Interested the object at least 30x30 pixels in size
)

print(f'Face found: {len(faces)}')

# 5) Drawing a frame if fond face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 6) Show result
cv2.imshow('Face Detection in Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()