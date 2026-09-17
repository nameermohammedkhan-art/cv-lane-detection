import json
from fpdf import FPDF
import os

class Report(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Road Lane Detection and Analysis - Project Report", align="C", ln=True)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, text):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 6, text)
        self.ln(5)

def main():
    pdf = Report()
    pdf.add_page()
    
    with open("outputs/metrics.json", "r") as f:
        metrics = json.load(f)
        
    sections = [
        ("1. Cover Page", "Project Title: Road Lane Detection and Analysis Using Classical Computer Vision\nCourse: VITyarthi Build Your Own Project\nStudent Name: Submitted for Review"),
        ("2. Introduction", "This project implements a command-line computer vision system to detect left and right road lane boundaries from images using purely classical image processing techniques without any machine learning or deep learning."),
        ("3. Problem Statement", "Understanding the road layout is a fundamental task for autonomous driving. While modern systems use deep learning, it is crucial to understand classical geometric approaches to line detection. This project builds an understandable, CPU-friendly pipeline to extract lane lines and evaluates it against a synthetically generated ground-truth dataset."),
        ("4. Functional Requirements", "- Generate synthetic road image dataset with known ground truth.\n- Detect edges and lines using classical CV techniques.\n- Extract, separate, and fit left and right lane boundaries.\n- Provide a CLI to run single-image and batch detections.\n- Automatically evaluate accuracy using Mean Absolute Error (MAE)."),
        ("5. Non-functional Requirements", "- Performance: Must run efficiently on a CPU using OpenCV.\n- Maintainability: Code must be modularized into discrete steps (preprocessing, edge detection, etc.).\n- Usability: Simple argparse CLI for executing all workflows.\n- Reliability: Graceful error handling for missing files and empty datasets."),
        ("6. System Architecture", "The system uses a sequential pipeline: Grayscale -> Gaussian Blur -> Canny Edge Detection -> ROI Masking -> Hough Transform -> Lane Separation -> Output Annotation."),
        ("7. Design Diagrams", "The system architecture and workflow are documented in Mermaid diagrams located in the 'docs/' directory. They outline the sequential pipeline and user interaction patterns via the CLI."),
        ("8. Design Decisions & Rationale", "A classical CV pipeline was chosen instead of ML to emphasize fundamental image processing concepts. A synthetic dataset was preferred so that exact ground-truth pixel coordinates could be used to calculate a precise MAE metric rather than relying on manual labeling."),
        ("9. Implementation Details", "The image is converted to grayscale before edge detection. The Canny operator is then applied to identify strong edges. A trapezoidal region is used as the region of interest to filter out background scenery. Detected Hough lines are divided into left and right groups using their slopes (positive/negative) and screen positions, and a degree 1 polynomial is fit to approximate the continuous lane lines."),
        ("10. Screenshots / Results", f"Actual evaluation on {metrics['total_images']} test images yielded the following results:\n- Left Lane Detection Rate: {metrics['left_lane_detection_rate']:.2f}\n- Right Lane Detection Rate: {metrics['right_lane_detection_rate']:.2f}\n- Left Lane MAE: {metrics['left_lane_mae']:.2f} pixels\n- Right Lane MAE: {metrics['right_lane_mae']:.2f} pixels\nOutput images with overlaid lane lines were successfully saved to the outputs/ directory."),
        ("11. Testing Approach", "Automated testing was conducted using Pytest. Tests verify that grayscale outputs are 2D, ROI masks properly occlude regions, Hough lines are successfully separated based on geometry, and the pipeline executes without crashing on valid inputs."),
        ("12. Challenges Faced", "Tuning Canny thresholds and Hough Line minimum lengths was challenging because noisy images caused spurious lines. Incorrect Hough lines sometimes confused the left/right lane separation, requiring stricter slope filtering (ignoring horizontal and near-vertical slopes)."),
        ("13. Learnings & Key Takeaways", "I learned how sensitive classical CV pipelines are to parameter changes and environmental noise. Separating geometric filtering (ROI masking) from pixel-intensity filtering (Canny) is critical for robust detection."),
        ("14. Future Enhancements", "Future enhancements could include implementing temporal smoothing to track lanes across multiple video frames, applying a perspective transformation to view lanes from a 'bird's eye' view, and utilizing curve fitting to detect non-straight lanes."),
        ("15. References", "- OpenCV Documentation (https://docs.opencv.org/)\n- NumPy Documentation (https://numpy.org/doc/)")
    ]
    
    for title, body in sections:
        pdf.chapter_title(title)
        pdf.chapter_body(body)
        
    os.makedirs("outputs", exist_ok=True)
    pdf.output("outputs/Project_Report.pdf")
    print("Report generated successfully.")

if __name__ == "__main__":
    main()
