import cv2
import numpy as np
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
root.destroy()
if image_path:
    img = cv2.imread(image_path, 0)
    if img is not None:
        kernel = np.ones((15, 15), np.uint8)
        result = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
        result = cv2.normalize(result, None, 0, 255, cv2.NORM_MINMAX)
        cv2.imshow("Original Image", img)
        cv2.imshow("Black Hat Image", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Black Hat operation completed successfully")
    else:
        print("Unable to read image")
else:
    print("No image selected")
