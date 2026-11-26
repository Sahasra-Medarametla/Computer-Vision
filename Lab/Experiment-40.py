import cv2
import pytesseract
from tkinter import Tk, filedialog
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
root = Tk()
root.withdraw()
video_path = filedialog.askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
root.destroy()
if video_path:
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    extracted_text = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % 30 == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray).strip()
            if text and text not in extracted_text:
                extracted_text.append(text)
                print("Extracted Text:", text)
        frame_count += 1
    cap.release()
    print("Text extraction completed successfully")
    if not extracted_text:
        print("No text found in the video")
else:
    print("No video selected")
