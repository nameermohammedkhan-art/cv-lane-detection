import cv2
from .preprocessing import convert_to_grayscale, apply_gaussian_blur
from .edge_detection import apply_canny
from .roi import get_roi_vertices, apply_roi_mask
from .lane_detection import detect_hough_lines, extract_lanes, draw_lanes

def process_image(img):
    """
    Main pipeline for processing an image to detect lanes.
    Returns the output image with lanes drawn, and the detected lane coordinates.
    """
    # 1. Grayscale
    gray = convert_to_grayscale(img)
    
    # 2. Gaussian Blur
    blur = apply_gaussian_blur(gray, kernel_size=5)
    
    # 3. Canny Edge Detection
    edges = apply_canny(blur, low_threshold=50, high_threshold=150)
    
    # 4. Region of Interest Masking
    roi_vertices = get_roi_vertices(img.shape)
    masked_edges = apply_roi_mask(edges, roi_vertices)
    
    # 5. Hough Line Transform
    lines = detect_hough_lines(masked_edges)
    
    # 6. Extract Lanes
    left_lane, right_lane = extract_lanes(lines, img.shape)
    
    # 7. Draw Lanes
    output_img = draw_lanes(img, left_lane, right_lane)
    
    return output_img, left_lane, right_lane
