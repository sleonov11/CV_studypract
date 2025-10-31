import cv2
import numpy as np


img = cv2.imread('pics/cat.jpg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[1]//2))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Используем метод Кенни, чтобы определить объект на рисунке
img = cv2.Canny(img, 90, 90)

kernel = np.ones((5,5), np.int8)
img = cv2.dilate(img, kernel, iterations = 1)

photo = np.zeros((450, 450, 3), dtype = 'uint8')
photo[:] = 250, 0 ,0 # перекрасили в синий цвет
cv2.imshow('pics/1.png', photo)




cv2.imshow('Result:', img)
#print(img.shape)
cv2.waitKey(50000)