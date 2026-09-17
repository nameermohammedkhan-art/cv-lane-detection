import cv2
import numpy as np

def detect_hough_lines(img, rho=1, theta=np.pi/180, threshold=20, min_line_len=20, max_line_gap=300):
    """Detects lines using the Hough Transform."""
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    if lines is None:
        return []
    return lines

def separate_lines(lines, img_width, img_height):
    """Separates lines into left and right lanes based on slope and position."""
    left_lines = []
    right_lines = []
    
    for item in lines:
        if len(item) == 1 and len(item[0]) == 4:
            x1, y1, x2, y2 = item[0]
        elif len(item) == 4:
            x1, y1, x2, y2 = item
        else:
            continue
            
        if x1 == x2:
            continue # Ignore vertical lines
        
        slope = (y2 - y1) / (x2 - x1)
        
        # Filter out extreme slopes (horizontal-ish or vertical-ish)
        if abs(slope) < 0.3 or abs(slope) > 10.0:
            continue
            
        if slope < 0 and x1 < img_width * 0.6 and x2 < img_width * 0.6:
            # Left lane: negative slope and mostly on the left side
            left_lines.append((x1, y1, x2, y2))
        elif slope > 0 and x1 > img_width * 0.4 and x2 > img_width * 0.4:
            # Right lane: positive slope and mostly on the right side
            right_lines.append((x1, y1, x2, y2))
            
    return left_lines, right_lines

def fit_lane_line(lines, img_height, roi_top):
    """Fits a single line to a group of line segments."""
    if not lines:
        return None
        
    x_coords = []
    y_coords = []
    for x1, y1, x2, y2 in lines:
        x_coords.extend([x1, x2])
        y_coords.extend([y1, y2])
        
    if not x_coords:
        return None
        
    # Fit a degree 1 polynomial (line): y = m*x + b -> x = (y - b)/m
    # It's better to fit x = f(y) to handle steep lines
    poly = np.polyfit(y_coords, x_coords, 1)
    
    y1 = img_height
    y2 = int(roi_top)
    
    x1 = int(np.polyval(poly, y1))
    x2 = int(np.polyval(poly, y2))
    
    return (x1, y1, x2, y2)

def extract_lanes(lines, img_shape):
    """Main function to extract left and right lane lines."""
    height, width = img_shape[:2]
    roi_top = height * 0.6
    
    left_lines, right_lines = separate_lines(lines, width, height)
    
    left_lane = fit_lane_line(left_lines, height, roi_top)
    right_lane = fit_lane_line(right_lines, height, roi_top)
    
    return left_lane, right_lane

def draw_lanes(img, left_lane, right_lane, color=(0, 255, 0), thickness=5):
    """Draws detected lane lines on an image."""
    line_img = np.zeros_like(img)
    if left_lane is not None:
        cv2.line(line_img, (left_lane[0], left_lane[1]), (left_lane[2], left_lane[3]), color, thickness)
    if right_lane is not None:
        cv2.line(line_img, (right_lane[0], right_lane[1]), (right_lane[2], right_lane[3]), color, thickness)
        
    # Overlay lines on the original image
    return cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)
