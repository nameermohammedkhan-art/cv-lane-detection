import numpy as np
import cv2
from src.lane_detection import detect_hough_lines, separate_lines, fit_lane_line

def test_detect_hough_lines():
    img = np.zeros((100, 100), dtype=np.uint8)
    cv2.line(img, (10, 10), (90, 90), 255, 2)
    lines = detect_hough_lines(img, threshold=10, min_line_len=10, max_line_gap=10)
    assert len(lines) > 0

def test_separate_lines():
    # Left line (negative slope)
    left = [[20, 100, 40, 60]]
    # Right line (positive slope)
    right = [[80, 100, 60, 60]]
    lines = left + right
    
    left_res, right_res = separate_lines(lines, 100, 100)
    assert len(left_res) == 1
    assert len(right_res) == 1

def test_fit_lane_line():
    lines = [(20, 100, 40, 60), (30, 80, 40, 60)]
    fit = fit_lane_line(lines, 100, 60)
    assert fit is not None
    assert len(fit) == 4
    assert fit[1] == 100
    assert fit[3] == 60
