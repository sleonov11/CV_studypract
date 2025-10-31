import cv2
cap = cv2.VideoCapture(0)
color_spaces = ('RGB', 'GRAY', 'HSV', 'LAB', 'XYZ', 'YUV')
cap.set(3, 500)
cap.set(5, 300)


while True:
    success, img = cap.read()
    color_images = {color: cv2.cvtColor(img, getattr(cv2, 'COLOR_BGR2' + color))
                    for color in color_spaces}
    for color in color_images:
        cv2.imshow(color, color_images[color])
    cv2.imshow('result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break