import cv2
import numpy as np
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
root.destroy()
if image_path:
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to read image!")
    else:
        h, w = img.shape[:2]
        src = np.float32([[0, 0], [w-1, 0], [0, h-1], [w-1, h-1]])
        dst = np.float32([[50, 30], [w-50, 30], [20, h-30], [w-20, h-30]])
        matrix = cv2.getPerspectiveTransform(src, dst)
        result = cv2.warpPerspective(img, matrix, (w, h))
        cv2.imshow("Original Image", img)
        cv2.imshow("Perspective Transformation", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Perspective transformation completed successfully!")
else:
    print("No image selected!")
