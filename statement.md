# Problem Statement

## Title
Road Lane Detection and Analysis Using Classical Computer Vision

## Objective
Detect left and right road lane boundaries from input images using traditional image-processing techniques, without relying on deep learning models.

## Scope
- Implement an image-processing pipeline using OpenCV.
- Convert images to grayscale and apply Gaussian blur to remove noise.
- Detect edges using the Canny edge detector.
- Mask the image to a defined region of interest (ROI) where the road is located.
- Extract straight line segments using the Hough Line Transform.
- Separate segments into left and right lanes based on their slopes.
- Draw solid lane lines on the original images.
- Provide a command-line interface to process single images or batches of images.
- Evaluate the accuracy of the detection against generated ground-truth data.

## Target Users
- Students and developers learning classical Computer Vision fundamentals.
- Researchers testing geometry-based lane detection pipelines on dashcam footage.
