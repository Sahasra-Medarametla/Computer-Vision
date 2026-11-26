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
        overlay = img.copy()
        cv2.putText(overlay, "SAMPLE WATERMARK", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        watermarked = cv2.addWeighted(overlay, 0.4, img, 0.6, 0)
        cv2.imshow("Original Image", img)
        cv2.imshow("Watermarked Image", watermarked)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Watermark added successfully!")
else:
    print("No image selected!")
