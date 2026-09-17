import pytest
import numpy as np
from src.preprocessing import convert_to_grayscale, apply_gaussian_blur

def test_convert_to_grayscale():
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    gray = convert_to_grayscale(img)
    assert len(gray.shape) == 2
    assert gray.shape == (100, 100)

def test_apply_gaussian_blur():
    img = np.zeros((100, 100), dtype=np.uint8)
    blur = apply_gaussian_blur(img, kernel_size=5)
    assert blur.shape == (100, 100)
    
def test_invalid_grayscale_input():
    img = np.zeros((100, 100), dtype=np.uint8) # Already grayscale
    with pytest.raises(ValueError):
        convert_to_grayscale(img)
