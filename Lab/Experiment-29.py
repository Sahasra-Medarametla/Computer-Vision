import cv2
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
root.destroy()
if image_path:
    img = cv2.imread(image_path)
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=6, minSize=(15, 15))
        for (x, y, w, h) in eyes:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("Number of eyes detected:", len(eyes))
        cv2.imshow("Eye Detection", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Unable to read image")
else:
    print("No image selected")
