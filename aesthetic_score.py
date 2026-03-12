import cv2
import numpy as np

def aesthetic_score(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return 0

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    saturation = hsv[:,:,1].mean() / 255
    brightness = hsv[:,:,2].mean() / 255
    contrast = img.std() / 255

    score = (0.4*brightness + 0.3*saturation + 0.3*contrast)
    return score