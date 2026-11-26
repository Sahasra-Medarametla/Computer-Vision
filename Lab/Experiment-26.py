import cv2
import os
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
video_path = filedialog.askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
root.destroy()
if video_path:
    cap = cv2.VideoCapture(video_path)
    frames = []
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    if frames:
        output_path = os.path.join(os.path.dirname(video_path), "reversed_video.mp4")
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))
        for frame in reversed(frames):
            out.write(frame)
            cv2.imshow("Reversed Video", frame)
            if cv2.waitKey(max(1, int(1000 / fps))) & 0xFF == ord('q'):
                break
        out.release()
        cv2.destroyAllWindows()
        print("Video reversed successfully")
        print("Saved at:", output_path)
    else:
        print("No frames found in video")
else:
    print("No video selected")
