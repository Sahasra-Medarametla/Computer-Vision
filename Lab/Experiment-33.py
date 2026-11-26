import cv2
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
root.destroy()
if image_path:
    img = cv2.imread(image_path)
    if img is not None:
        h, w = img.shape[:2]
        cv2.rectangle(img, (50, 50), (w-50, h-50), (0, 255, 0), 3)
        cv2.imshow("Rectangle on Image", img)
        cv2.imwrite("rectangle_output.jpg", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Rectangle drawn and image saved successfully")
    else:
        print("Unable to read image")
else:
    print("No image selected")
