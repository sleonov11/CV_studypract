import cv2
face_cascade = cv2.CascadeClassifier('face.xml')
image = cv2.imread('pics/face.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,
                                      minSize=(30,30))
for(x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+w), (0,255,0), 2)

cv2.imshow('res',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
cap = cv2.VideoCapture('video.mp4')

while True:
    ret,frame = cap.read()
    if ret:
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""