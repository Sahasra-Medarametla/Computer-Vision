import cv2
import numpy as np
img = np.full((500, 700, 3), 255, dtype=np.uint8)
h, w = img.shape[:2]
box_w = w // 10
box_h = h // 10
cv2.rectangle(img, (0, 0), (box_w, box_h), (0, 0, 255), -1)
cv2.rectangle(img, (w-box_w, 0), (w-1, box_h), (0, 255, 0), -1)
cv2.rectangle(img, (0, h-box_h), (box_w, h-1), (255, 0, 0), -1)
cv2.rectangle(img, (w-box_w, h-box_h), (w-1, h-1), (0, 255, 255), -1)
cv2.imshow("White Image with Four Coloured Corner Boxes", img)
cv2.imwrite("four_corner_boxes.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Image created and saved successfully")
