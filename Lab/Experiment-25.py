import cv2
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
template_path = filedialog.askopenfilename(title="Select Watch Template Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
image_path = filedialog.askopenfilename(title="Select Image to Search", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
root.destroy()
if template_path and image_path:
    template = cv2.imread(template_path, 0)
    img = cv2.imread(image_path)
    if template is not None and img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w = template.shape
        H, W = gray.shape
        scale = min(W / w, H / h, 1.0)
        template = cv2.resize(template, (int(w * scale), int(h * scale)))
        h, w = template.shape
        result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if max_val > 0.6:
            cv2.rectangle(img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 3)
            print("Watch recognized successfully")
            print("Matching confidence:", round(max_val, 2))
        else:
            print("Watch not found")
            print("Matching confidence:", round(max_val, 2))
        cv2.imshow("Watch Recognition", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Unable to read selected images")
else:
    print("Image selection cancelled")
