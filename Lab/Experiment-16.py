import cv2
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
        gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        abs_x = cv2.convertScaleAbs(gx)
        abs_y = cv2.convertScaleAbs(gy)
        sobel = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
        cv2.imshow("Original Image", img)
        cv2.imshow("Sobel X", abs_x)
        cv2.imshow("Sobel Y", abs_y)
        cv2.imshow("Sobel Filtered Image", sobel)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Sobel filtering completed successfully!")
else:
    print("No image selected!")
