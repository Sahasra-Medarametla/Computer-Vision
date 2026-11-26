import cv2
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
        height, width = img.shape[:2]
        print("Original Size:", width, "x", height)
        bigger = cv2.resize(
            img, None, fx=1.5, fy=1.5,
            interpolation=cv2.INTER_LINEAR
        )
        smaller = cv2.resize(
            img, None, fx=0.5, fy=0.5,
            interpolation=cv2.INTER_AREA
        )
        cv2.imshow("Original Image", img)
        cv2.imshow("Bigger Image", bigger)
        cv2.imshow("Smaller Image", smaller)
        print("Bigger Size:", bigger.shape[1], "x", bigger.shape[0])
        print("Smaller Size:", smaller.shape[1], "x", smaller.shape[0])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Image scaling completed successfully!")
else:
    print("No image selected!")
