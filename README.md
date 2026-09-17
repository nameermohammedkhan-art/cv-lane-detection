# Road Lane Detection and Analysis Using Classical Computer Vision

## Overview

This project detects the left and right lane lines in road images. It uses OpenCV operations such as grayscale conversion, Gaussian blur, Canny edge detection, a region of interest mask, and the Hough transform. 

## Features

- Download and extract real-world road frames from a dashcam video
- Preprocess the images (grayscale and blur)
- Detect edges using Canny
- Apply a region of interest (ROI) mask
- Detect lane lines using Hough transform
- Classify lines into left and right lanes based on slope
- Save detected images with lane overlays
- Evaluate detection yield across the dataset

## Technologies

- Python 3
- `opencv-python` (cv2)
- `numpy`
- `pytest`
- `fpdf`

## Project Structure

- `src/` - Core image processing code (edge detection, ROI, lane extraction)
- `tests/` - Pytest unit tests for the processing modules
- `scripts/` - Scripts for downloading data and building the PDF report
- `docs/` - System diagrams (architecture, workflow, use case, class diagrams)
- `data/` - Holds downloaded real-world dashcam frames
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

The project relies on a real-world driving dataset. The `download_real_data.py` script downloads a standard dashcam video (from the Udacity Self-Driving Car dataset) and extracts it into 681 real-world JPEG frames located in `data/test`.

## Running the Project

**Download and extract the dataset:**
```bash
python scripts/download_real_data.py
```

**Run lane detection on a single image:**
```bash
python main.py --detect data/test/frame_0300.jpg
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

When evaluated on the 681 real-world video frames (`python main.py --evaluate data/test`), the pipeline achieved a 100% detection rate (tracking yield) for both left and right lanes.

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
