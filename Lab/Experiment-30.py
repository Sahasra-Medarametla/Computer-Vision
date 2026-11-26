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
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
        faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(60, 60))
        count = 0
        for (x, y, w, h) in faces:
            roi_gray = gray[y + h//2:y + h, x:x + w]
            roi_color = img[y + h//2:y + h, x:x + w]
            smiles = smile_cascade.detectMultiScale(roi_gray, 1.5, 15, minSize=(25, 15))
            if len(smiles) > 0:
                sx, sy, sw, sh = max(smiles, key=lambda s: s[2] * s[3])
                cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
                count += 1
        print("Number of smiles detected:", count)
        cv2.imshow("Smile Detection", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Unable to read image")
else:
    print("No image selected")
