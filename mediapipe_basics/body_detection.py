import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5)

image = cv2.imread('face.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
result = pose.process(image)
mp_drawing = mp.solutions.drawing_utils
annotated_image = image.copy()
mp_drawing.draw_landmarks(annotated_image, result.pose_landmarks,
                          mp_pose.POSE_CONNECTIONS)

cv2.imshow('mediapipe pose', annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()