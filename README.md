# Road Lane Detection and Analysis Using Classical Computer Vision

## Overview
This project implements a command-line computer vision system designed to detect left and right road lane boundaries from images. Instead of using deep learning or pre-trained models, the system strictly relies on classical image processing techniques to extract and estimate lane lines. It uses a synthetically generated dataset for testing and quantitative evaluation.

## Features
- **Classical Computer Vision Pipeline:** Uses fundamental techniques such as Grayscale conversion, Gaussian Blur, Canny Edge Detection, Region of Interest (ROI) masking, and the Hough Line Transform.
- **Synthetic Dataset Generation:** Includes a script to generate a reproducible synthetic dataset of road images with known ground-truth lane parameters, complete with varying slopes, noise, and blur.
- **Command-Line Interface (CLI):** Provides a simple argparse-based CLI for data generation, single-image detection, batch detection, and quantitative evaluation.
- **Quantitative Evaluation:** Compares detected lane parameters against ground-truth data to calculate Mean Absolute Error (MAE) and detection rates.
- **Modular Codebase:** Organizes operations into clear, single-responsibility Python modules.

## Technologies Used
- Python 3
- OpenCV (`cv2`)
- NumPy
- Pytest

## Project Structure
```
├── data/                  # Generated synthetic datasets (train, val, test)
├── docs/                  # Design diagrams
├── outputs/               # Saved output images and metrics
├── scripts/
│   └── prepare_data.py    # Script to generate synthetic road images
├── src/
│   ├── edge_detection.py  # Canny edge detection
│   ├── evaluation.py      # Error and metric calculations
│   ├── lane_detection.py  # Hough transform and line separation
│   ├── pipeline.py        # Connects the processing steps
│   ├── preprocessing.py   # Grayscale and blur functions
│   ├── roi.py             # Region of Interest masking
│   └── utils.py           # Helper functions for files/images
├── tests/                 # Pytest unit tests for modules
├── main.py                # CLI entry point
├── README.md              # Project documentation
└── statement.md           # Problem statement and scope
```

## Requirements
To run this project, install the required dependencies:
```bash
pip install opencv-python numpy pytest
```

## Dataset Generation
The project relies on a synthetic dataset for reproducibility. Generate the data locally using the following command:
```bash
python scripts/prepare_data.py --num 600
```
This creates 600 images split into `train`, `val`, and `test` directories inside the `data/` folder, along with JSON files containing ground-truth coordinates.

## Running the Project
Use `main.py` to interact with the system.

**1. Detect lanes in a single image:**
```bash
python main.py --detect data/test/image_0510.png
```

**2. Detect lanes in a batch of images:**
```bash
python main.py --batch-detect data/test/
```
The processed images with lane overlays are saved in `outputs/detected/`.

## Evaluation
To evaluate the system against the known ground-truth parameters in the test set, run:
```bash
python main.py --evaluate
```
This calculates the Left and Right Lane Detection Rates and Mean Absolute Error (MAE), saving the results to `outputs/metrics.json`.

## Testing
The project uses Pytest to verify functional behavior. Run the tests with:
```bash
python -m pytest tests/
```

## Example Output
When running the detection on an image, the CLI outputs details such as:
```text
Input: data/test/image_0510.png
Left lane detected: yes
Right lane detected: yes
Output: outputs/detected/image_0510.png
```

## Limitations
- The system struggles slightly with extreme lane curvature or varying lighting conditions since thresholds for Canny and Hough transforms are fixed.
- Because it uses classical geometric filtering, lines that are too short or obscured by heavy noise may not be grouped correctly into left or right lanes.
