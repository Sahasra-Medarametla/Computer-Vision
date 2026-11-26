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
        src = np.float32([[50, 50], [w-50, 50], [50, h-50]])
        dst = np.float32([[20, 80], [w-80, 50], [80, h-50]])
        matrix = cv2.getAffineTransform(src, dst)
        result = cv2.warpAffine(img, matrix, (w, h))
        cv2.imshow("Original Image", img)
        cv2.imshow("Affine Transformation", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Affine transformation completed successfully!")
else:
    print("No image selected!")
