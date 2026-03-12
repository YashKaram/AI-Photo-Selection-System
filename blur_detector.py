import cv2

def blur_score(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return 0

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()

    return variance