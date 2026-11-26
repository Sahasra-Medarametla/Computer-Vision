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
        rotated = cv2.rotate(
            img, cv2.ROTATE_90_CLOCKWISE
        )
        cv2.imshow("Original Image", img)
        cv2.imshow("90 Degree Clockwise Rotation", rotated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("90-degree clockwise rotation completed successfully!")
else:
    print("No image selected!")
