# Road Lane Detection and Analysis Using Classical Computer Vision

## Overview

This project detects the left and right lane lines in road images. It uses OpenCV operations such as grayscale conversion, Gaussian blur, Canny edge detection, a region of interest mask, and the Hough transform. 

## Features

- Generate synthetic road images with noise and variable lane slopes
- Download and extract real-world road frames from a dashcam video
- Preprocess the images (grayscale and blur)
- Detect edges using Canny
- Apply a region of interest (ROI) mask
- Detect lane lines using Hough transform
- Classify lines into left and right lanes based on slope
- Save detected images with lane overlays
- Compare detections with generated ground truth (calculate MAE and detection yield)

## Technologies

- Python 3
- `opencv-python` (cv2)
- `numpy`
- `pytest`
- `fpdf`

## Project Structure

- `src/` - Core image processing code (edge detection, ROI, lane extraction)
- `tests/` - Pytest unit tests for the processing modules
- `scripts/` - Scripts for generating data and building the PDF report
- `docs/` - System diagrams (architecture, workflow, use case, class diagrams)
- `data/` - Holds generated synthetic images and downloaded real-world frames
- `outputs/` - Saved output images and evaluation metrics
- `main.py` - Command-line interface for the project
- `requirements.txt` - Project dependencies

## Installation

Create and activate a virtual environment:

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:
```bash
pip install -r requirements.txt
```

## Dataset Generation

The project includes two data sources:

1. **Synthetic Dataset:** 
   The script generates 600 synthetic road images. The images are split into train, validation, and test folders (420/90/90). The lane position, slope, noise, and blur are randomly changed between images. Ground-truth coordinates are stored in a JSON file (`_labels.json`) alongside the generated dataset.
   
2. **Real-world Dataset:** 
   Another script downloads a standard dashcam video (from the Udacity Self-Driving Car dataset) and extracts it into 681 real-world JPEG frames.

## Running the Project

**Generate the synthetic dataset (600 images):**
```bash
python scripts/prepare_data.py --num 600
```

**Download and extract the real-world dataset:**
```bash
python scripts/download_real_data.py
```

**Run lane detection on a single image:**
```bash
python main.py --detect data/test/image_0510.png
```

**Run batch detection on a directory:**
```bash
python main.py --batch-detect data/test
```

**Run evaluation against the test set:**
```bash
python main.py --evaluate
```

**Generate the PDF report:**
```bash
python scripts/build_exact_report.py
```

## Results

The evaluation compares the detected lane coordinates with the generated ground truth on the 90 synthetic test images.

The current test results are shown below:
- **Left Lane Detection Rate:** 87.0%
- **Right Lane Detection Rate:** 71.0%
- **Overall Mean Absolute Error (MAE):** 15.54 pixels

When evaluated on the 681 real-world video frames (`python main.py --evaluate data/real_dataset`), the pipeline achieved a 100% detection rate (tracking yield) for both left and right lanes.

## Testing

Pytest tests are included for preprocessing, edge detection, ROI processing, lane geometry logic, and the main pipeline.

Running `pytest tests/` returns:
```text
tests\test_edge_detection.py .
tests\test_lane_detection.py ...
tests\test_pipeline.py .
tests\test_preprocessing.py ...
tests\test_roi.py ..
============================= 10 passed in 0.10s ==============================
```

## Limitations

- Fixed Canny thresholds and Hough parameters may fail when the lane is heavily blurred or the lighting changes significantly.
- The region of interest mask assumes a centered, forward-facing dashboard camera. It cuts off the top half of the image. If the camera angle changes, the ROI coordinates in `src/roi.py` must be updated.
- The pipeline relies on straight line equations (1D polyfit), so it struggles to draw accurate overlays on sharp, continuous curves.
