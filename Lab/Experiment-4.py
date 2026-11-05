import cv2
import matplotlib.pyplot as plt
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
        equalized = cv2.equalizeHist(gray)
        cv2.imshow("Original Grayscale Image", gray)
        cv2.imshow("Histogram Equalized Image", equalized)
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.hist(gray.ravel(), 256, [0, 256])
        plt.title("Original Histogram")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Frequency")
        plt.subplot(1, 2, 2)
        plt.hist(equalized.ravel(), 256, [0, 256])
        plt.title("Equalized Histogram")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("No image selected!")
