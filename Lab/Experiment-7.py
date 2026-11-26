import cv2
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
video_path = filedialog.askopenfilename(
    title="Select a Video",
    filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
)
root.destroy()
if video_path:
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video!")
    else:
        print("Press 1 for Normal Motion")
        print("Press 2 for Slow Motion")
        print("Press 3 for Fast Motion")
        print("Press Q to Exit")
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Video Processing", frame)
            key = cv2.waitKey(30) & 0xFF
            if key == ord('1'):
                delay = 30
            elif key == ord('2'):
                delay = 150
            elif key == ord('3'):
                delay = 1
            elif key == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
else:
    print("No video selected!")
