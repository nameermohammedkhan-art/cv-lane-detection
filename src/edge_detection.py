import cv2

def apply_canny(img, low_threshold=50, high_threshold=150):
    """Applies Canny edge detection to an image."""
    return cv2.Canny(img, low_threshold, high_threshold)
