import cv2
from mediapipe.python.solutions.face_detection import FaceDetection

def face_score(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return 0

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    with FaceDetection(
        model_selection=1,
        min_detection_confidence=0.5
    ) as detector:

        result = detector.process(rgb)

        if result.detections:
            return 1
        else:
            return 0