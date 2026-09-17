import numpy as np
from src.roi import get_roi_vertices, apply_roi_mask

def test_get_roi_vertices():
    shape = (480, 640, 3)
    vertices = get_roi_vertices(shape)
    assert vertices.shape == (1, 4, 2)
    assert vertices[0][0][1] == 480 # Bottom left y

def test_apply_roi_mask():
    img = np.ones((100, 100), dtype=np.uint8) * 255
    vertices = np.array([[[10, 100], [40, 60], [60, 60], [90, 100]]], dtype=np.int32)
    masked = apply_roi_mask(img, vertices)
    
    assert masked.shape == (100, 100)
    assert masked[10, 10] == 0 # Outside ROI should be 0
    assert masked[80, 50] == 255 # Inside ROI should be 255
