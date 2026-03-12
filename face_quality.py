import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh

def _get_landmarks(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None, None

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        result = face_mesh.process(rgb)

        if not result.multi_face_landmarks:
            return None, None

        h, w, _ = img.shape
        pts = result.multi_face_landmarks[0].landmark
        coords = np.array([(int(p.x*w), int(p.y*h)) for p in pts])

        return img, coords


def smile_score(image_path):
    img, pts = _get_landmarks(image_path)
    if pts is None:
        return 0

    # mouth corners
    left = pts[61]
    right = pts[291]
    top = pts[13]
    bottom = pts[14]

    width = np.linalg.norm(left-right)
    height = np.linalg.norm(top-bottom)

    ratio = height / width
    return min(ratio*3,1)


def eyes_open_score(image_path):
    img, pts = _get_landmarks(image_path)
    if pts is None:
        return 0

    # left eye
    top = pts[159]
    bottom = pts[145]
    left = pts[33]
    right = pts[133]

    height = np.linalg.norm(top-bottom)
    width = np.linalg.norm(left-right)

    ratio = height/width
    return min(ratio*4,1)