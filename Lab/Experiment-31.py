import cv2
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
root.destroy()
if image_path:
    img = cv2.imread(image_path, 0)
    if img is not None:
        _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        _, inverse = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
        cv2.imshow("Original Image", img)
        cv2.imshow("Binary Segmentation", binary)
        cv2.imshow("Inverse Segmentation", inverse)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Image segmentation completed successfully")
    else:
        print("Unable to read image")
else:
    print("No image selected")
