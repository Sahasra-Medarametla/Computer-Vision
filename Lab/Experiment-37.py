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
        lower = np.array([0, 0, 0])
        upper = np.array([180, 255, 179])
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow("Original Image", img)
        cv2.imshow("Foreground Mask", mask)
        cv2.imshow("Foreground Subtracted Image", result)
        cv2.imwrite("foreground_subtracted.jpg", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Foreground subtraction completed successfully")
        print("Output saved as foreground_subtracted.jpg")
    else:
        print("Unable to read image")
else:
    print("No image selected")
