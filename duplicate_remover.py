from PIL import Image
import imagehash

def remove_duplicates(image_paths, threshold=5):
    unique = []
    hashes = []

    for path in image_paths:
        img = Image.open(path)
        h = imagehash.phash(img)

        duplicate = False
        for existing in hashes:
            if abs(h - existing) < threshold:
                duplicate = True
                break

        if not duplicate:
            unique.append(path)
            hashes.append(h)

    return unique