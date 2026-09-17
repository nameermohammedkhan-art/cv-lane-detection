import os
import urllib.request
import cv2

def download_and_extract():
    video_url = "https://raw.githubusercontent.com/udacity/CarND-LaneLines-P1/master/test_videos/solidYellowLeft.mp4"
    video_path = "solidYellowLeft.mp4"
    output_dir = "data/test"
    
    os.makedirs(output_dir, exist_ok=True)
    
    print("Downloading real-world driving video...")
    urllib.request.urlretrieve(video_url, video_path)
    
    print("Extracting frames to use as the dataset...")
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Save frame
        frame_path = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_count += 1
        
    cap.release()
    print(f"Successfully extracted {frame_count} real road images to {output_dir}")

if __name__ == "__main__":
    download_and_extract()
