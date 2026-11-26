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
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        corners = cv2.cornerHarris(gray, 2, 3, 0.04)
        result = cv2.imread(image_path)
        result[corners > 0.01 * corners.max()] = [0, 0, 255]
        cv2.imshow("Original Image", cv2.imread(image_path))
        cv2.imshow("Harris Corner Detection", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Harris corner detection completed successfully!")
else:
    print("No image selected!")
