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
        blue, green, red = cv2.split(img)
        blue_hist = cv2.calcHist([blue], [0], None, [256], [0, 256])
        green_hist = cv2.calcHist([green], [0], None, [256], [0, 256])
        red_hist = cv2.calcHist([red], [0], None, [256], [0, 256])
        plt.plot(blue_hist, label="Blue")
        plt.plot(green_hist, label="Green")
        plt.plot(red_hist, label="Red")
        plt.title("Color Histogram")
        plt.xlabel("Color Intensity (0-255)")
        plt.ylabel("Number of Pixels")
        plt.legend()
        plt.grid()
        plt.show()
        print("Color histogram analyzed successfully!")
else:
    print("No image selected!")
