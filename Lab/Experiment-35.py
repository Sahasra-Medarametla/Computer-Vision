import cv2
from tkinter import Tk, filedialog, simpledialog
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
if image_path:
    text = simpledialog.askstring("Enter Text", "Enter the text to display on the image:")
    img = cv2.imread(image_path)
    if img is not None and text:
        cv2.putText(img, text, (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Text on Image", img)
        cv2.imwrite("text_output.jpg", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Text added and image saved successfully")
    else:
        print("Invalid image or no text entered")
else:
    print("No image selected")
root.destroy()
