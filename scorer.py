from blur_detector import blur_score
from face_detector import face_score
from face_quality import smile_score, eyes_open_score
from aesthetic_score import aesthetic_score
from face_count import count_faces

def total_score(image_path, mode="Mixed"):

    b = blur_score(image_path)
    blur_norm = min(b/1000,1)

    f = face_score(image_path)
    s = smile_score(image_path)
    e = eyes_open_score(image_path)
    a = aesthetic_score(image_path)
    fc = count_faces(image_path)

    # -------- SINGLE --------
    if mode == "Single":
        score = (
            0.3*f +
            0.25*s +
            0.2*e +
            0.15*a +
            0.1*blur_norm
        )

    # -------- GROUP --------
    elif mode == "Group":
        face_factor = min(fc/5,1)  # normalize faces
        score = (
            0.35*face_factor +
            0.25*e +
            0.2*s +
            0.1*a +
            0.1*blur_norm
        )

    # -------- MIXED --------
    else:
        score = (
            0.25*blur_norm +
            0.25*f +
            0.2*s +
            0.15*e +
            0.15*a
        )

    return score