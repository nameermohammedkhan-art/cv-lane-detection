# Problem Statement

## Problem Statement
Modern autonomous driving systems rely heavily on complex machine learning models to understand the road. However, these models can be opaque and computationally expensive. There is significant educational and practical value in understanding how fundamental, classical computer vision techniques can be used to extract geometric lane information from road images without relying on deep learning.

## Scope
The scope of this project is limited to identifying and drawing left and right lane boundaries on road images using a classical computer vision pipeline. The system processes static images, applies geometric and edge-based filters, extracts lines, and classifies them into left or right lanes. The project also includes a localized data generation script to provide a controllable synthetic dataset for repeatable quantitative evaluation. Real-time video processing and curved lane fitting are outside the scope.

## Target Users
- Students learning fundamental computer vision concepts.
- Developers looking for a lightweight, CPU-friendly lane detection baseline.
- Researchers interested in the geometric evaluation of line-detection algorithms.

## High-Level Features
- Extensible, modular Python pipeline for image processing.
- Synthetic road image generator with configurable noise, blur, and slope variation.
- Command-line interface for single-image, batch-image, and evaluation workflows.
- Configurable Region of Interest (ROI) and Hough Transform parameters.
- Quantitative evaluation calculating detection rate and Mean Absolute Error (MAE) based on known ground-truth coordinates.
