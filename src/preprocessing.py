import cv2

def convert_to_grayscale(img):
    """Converts a BGR image to grayscale."""
    if len(img.shape) != 3 or img.shape[2] != 3:
        raise ValueError("Input image must be a 3-channel BGR image.")
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def apply_gaussian_blur(img, kernel_size=5):
    """Applies Gaussian blur to an image."""
    if kernel_size % 2 == 0 or kernel_size <= 0:
        raise ValueError("Kernel size must be a positive odd integer.")
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
