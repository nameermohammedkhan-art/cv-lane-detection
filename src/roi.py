import cv2
import numpy as np

def get_roi_vertices(image_shape):
    """Calculates trapezoidal ROI vertices based on image dimensions."""
    height, width = image_shape[:2]
    bottom_left = (int(width * 0.1), height)
    top_left = (int(width * 0.4), int(height * 0.6))
    top_right = (int(width * 0.6), int(height * 0.6))
    bottom_right = (int(width * 0.9), height)
    return np.array([[bottom_left, top_left, top_right, bottom_right]], dtype=np.int32)

def apply_roi_mask(img, vertices):
    """Applies a polygonal mask to the image."""
    mask = np.zeros_like(img)
    
    # If the image has multiple channels, define a multi-channel mask value
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image
