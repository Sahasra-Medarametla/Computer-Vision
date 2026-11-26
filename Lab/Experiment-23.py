import cv2
import numpy as np
img = np.zeros((400, 600), dtype=np.uint8)
cv2.rectangle(img, (100, 100), (250, 300), 255, -1)
cv2.circle(img, (400, 200), 80, 255, -1)
cv2.circle(img, (400, 200), 20, 0, -1)
kernel = np.ones((55, 55), np.uint8)
result = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Original Image", img)
cv2.imshow("Top Hat Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Top Hat operation completed successfully")
