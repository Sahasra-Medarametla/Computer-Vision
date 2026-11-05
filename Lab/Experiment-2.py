import cv2
img = cv2.imread("D:\WORD DOCUMENTS\Computer Vision\Lab\input.jpg")
if img is None:
    print("Error: Image not found!")
else:
    blur = cv2.GaussianBlur(img, (19, 19), 0)
    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blur Image", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
