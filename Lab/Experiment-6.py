import cv2
import numpy as np
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)
root.destroy()
if image_path:
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to read image!")
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(
            gray, 127, 255, cv2.THRESH_BINARY
        )
        kernel = np.ones((5, 5), np.uint8)
        eroded = cv2.erode(
            binary, kernel, iterations=1
        )
        cv2.imshow("Original Binary Image", binary)
        cv2.imshow("Eroded Image", eroded)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Image erosion completed successfully!")
else:
    print("No image selected!")
