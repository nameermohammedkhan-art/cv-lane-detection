import numpy as np
import cv2
from src.pipeline import process_image

def test_process_image():
    # Create a dummy road image
    img = np.ones((480, 640, 3), dtype=np.uint8) * 100
    cv2.line(img, (200, 480), (300, 300), (255, 255, 255), 5)
    cv2.line(img, (440, 480), (340, 300), (255, 255, 255), 5)
    
    out_img, left_lane, right_lane = process_image(img)
    
    assert out_img.shape == (480, 640, 3)
    # The pipeline should detect at least one lane from this ideal synthetic image
    assert left_lane is not None or right_lane is not None
