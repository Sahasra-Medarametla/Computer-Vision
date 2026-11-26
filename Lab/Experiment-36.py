import cv2
import numpy as np
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
root.destroy()
if image_path:
    img = cv2.imread(image_path)
    if img is not None:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = np.array([0, 0, 180])
        upper = np.array([180, 60, 255])
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))
        background = np.zeros_like(img)
        cv2.imshow("Original Image", img)
        cv2.imshow("Background Mask", mask)
        cv2.imshow("Background Subtracted Image", result)
        cv2.imwrite("background_subtracted.jpg", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Background subtraction completed successfully")
        print("Output saved as background_subtracted.jpg")
    else:
        print("Unable to read image")
else:
    print("No image selected")
