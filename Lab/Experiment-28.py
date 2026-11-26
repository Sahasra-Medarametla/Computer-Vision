import cv2
import os
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
video_path = filedialog.askopenfilename(title="Select a Traffic Video", filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
root.destroy()
if video_path:
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output_path = os.path.join(os.path.dirname(video_path), "detected_vehicles.mp4")
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))
    background = cv2.createBackgroundSubtractorMOG2()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        mask = background.apply(frame)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        count = 0
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if cv2.contourArea(contour) > 1500 and w > 40 and h > 30:
                count += 1
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, "Vehicle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(frame, "Detected Objects: " + str(count), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        out.write(frame)
        cv2.imshow("Vehicle Detection", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Vehicle detection completed successfully")
    print("Detected video saved at:", output_path)
else:
    print("No video selected")
