import cv2
import mediapipe as mp

mp_face = mp.solutions.face_detection

def count_faces(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return 0

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    with mp_face.FaceDetection(model_selection=1) as detector:
        result = detector.process(rgb)

        if result.detections:
            return len(result.detections)
        return 0