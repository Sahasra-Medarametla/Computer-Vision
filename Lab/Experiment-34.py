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
        center = (w // 2, h // 2)
        radius = min(w, h) // 4
        cv2.circle(img, center, radius, (0, 0, 255), 3)
        cv2.imshow("Circle on Image", img)
        cv2.imwrite("circle_output.jpg", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Circle drawn and image saved successfully")
    else:
        print("Unable to read image")
else:
    print("No image selected")
