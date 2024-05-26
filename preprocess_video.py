import mediapipe as mp
import numpy as np
import cv2

def main():

    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    pose =  mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) 
        
    video_dir = "./walk.mp4"

    cap = cv2.VideoCapture(video_dir)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOE_BGR2RGB)
        results = pose.process(frame)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        height,width = frame.shape[0],frame.shape[1]
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())