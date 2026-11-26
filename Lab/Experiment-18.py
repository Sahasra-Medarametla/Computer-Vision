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
        h, w = img.shape[:2]
        roi = img[50:min(150,h), 50:min(150,w)].copy()
        result = img.copy()
        rh, rw = roi.shape[:2]
        if h >= rh + 200 and w >= rw + 200:
            result[200:200+rh, 200:200+rw] = roi
            cv2.imshow("Original Image", img)
            cv2.imshow("Cropped ROI", roi)
            cv2.imshow("Copied and Pasted Image", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print("Cropping, copying and pasting completed successfully!")
        else:
            print("Select an image with dimensions greater than 300 x 300 pixels.")
else:
    print("No image selected!")
