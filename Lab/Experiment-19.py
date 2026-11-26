import cv2
import numpy as np
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
root.destroy()
if image_path:
    img = cv2.imread(image_path, 0)
    if img is None:
        print("Error: Unable to read image!")
    else:
        _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        kernel = np.ones((5, 5), np.uint8)
        result = cv2.morphologyEx(binary, cv2.MORPH_ERODE, kernel)
        cv2.imshow("Original Binary Image", binary)
        cv2.imshow("Morphological Erosion", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Morphological erosion completed successfully!")
else:
    print("No image selected!")
