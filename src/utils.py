import os
import cv2

def ensure_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def load_image(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Image not found: {filepath}")
    img = cv2.imread(filepath)
    if img is None:
        raise ValueError(f"Failed to load image: {filepath}")
    return img

def save_image(filepath, img):
    ensure_dir(os.path.dirname(filepath))
    cv2.imwrite(filepath, img)
