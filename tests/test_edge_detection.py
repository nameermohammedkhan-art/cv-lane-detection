import numpy as np
from src.edge_detection import apply_canny

def test_apply_canny():
    img = np.zeros((100, 100), dtype=np.uint8)
    img[40:60, 40:60] = 255
    edges = apply_canny(img, 50, 150)
    assert edges.shape == (100, 100)
    assert np.any(edges > 0) # Should detect some edges
