from fpdf import FPDF

class ExactReport(FPDF):
    def header(self):
        pass # No header
    
    def footer(self):
        pass # No footer

def create_report():
    pdf = ExactReport(format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # --- PAGE 1 ---
    pdf.add_page()
    pdf.set_y(100)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "VITyarthi - Computer Vision Project Report", align="C", ln=True)
    pdf.ln(10)
    
    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 15, "Road Lane Detection and Analysis", align="C", ln=True)
    pdf.set_font("Arial", "", 16)
    pdf.cell(0, 10, "Using Classical Computer Vision", align="C", ln=True)
    
    pdf.set_y(220)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "Nameer Mohammed Khan", align="C", ln=True)
    pdf.cell(0, 8, "24BAI10892", align="C", ln=True)
    
    # --- PAGE 2 ---
    pdf.add_page()
    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "1. Introduction", ln=True)
    pdf.set_font("Arial", "", 11)
    intro_text = "This project detects the left and right lane lines in road images. It uses OpenCV operations such as grayscale conversion, Gaussian blur, Canny edge detection, a region of interest mask, and the Hough transform."
    pdf.multi_cell(0, 6, intro_text)
    pdf.ln(10)
    
    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "2. Problem Statement", ln=True)
    pdf.set_font("Arial", "", 11)
    prob_text = "The goal is to detect road lanes from images using classical CV techniques, demonstrating line extraction and geometric fitting in a Python pipeline."
    pdf.multi_cell(0, 6, prob_text)
    pdf.ln(10)
    
    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "3. Functional Requirements", ln=True)
    pdf.set_font("Arial", "", 11)
    reqs = [
        "- Generate synthetic road images or extract real-world dashcam frames.",
        "- Process images using grayscale conversion and Gaussian filtering.",
        "- Detect edges using Canny edge detection and apply ROI masks.",
        "- Extract lane lines using Hough Line Transform.",
        "- Classify lanes as Left or Right using slopes.",
        "- Provide a CLI for batch detection and evaluation."
    ]
    for r in reqs:
        pdf.cell(0, 6, r, ln=True)
    pdf.ln(10)

    # --- PAGE 3 ---
    pdf.add_page()
    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "4. Use Cases", ln=True)
    pdf.set_font("Arial", "", 11)
    use_cases = [
        "- Run lane detection on a single image.",
        "- Run batch detection on a directory of images.",
        "- Evaluate detection accuracy against ground truth data."
    ]
    for uc in use_cases:
        pdf.cell(0, 6, uc, ln=True)
    pdf.ln(10)
    
    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "5. System Architecture & 6. Design Diagrams", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 6, "Below are the system diagrams generated using cv2 drawing primitives:", ln=True)
    pdf.ln(5)
    
    pdf.image("docs/arch.png", x=20, w=170)
    pdf.ln(10)
    pdf.image("docs/flow.png", x=20, w=170)
    
    # --- PAGE 4 ---
    pdf.add_page()
    pdf.image("docs/usecase.png", x=20, w=170)
    pdf.ln(10)
    pdf.image("docs/class.png", x=20, w=170)
    pdf.ln(15)

    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "7. Design Decisions & Rationale", ln=True)
    pdf.set_font("Arial", "", 11)
    rationale = "Both synthetic and real-world datasets were used to test the system. A custom lane extraction algorithm was written to use classical CV instead of deep learning. Geometric slope filtering was used to split the Hough lines into left and right lanes."
    pdf.multi_cell(0, 6, rationale)
    pdf.ln(10)
    
    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "8. Implementation Details", ln=True)
    pdf.set_font("Arial", "", 11)
    impl = "OpenCV is used for image operations. Images are converted to grayscale and blurred. Canny edge detection finds structural outlines, followed by an ROI trapezoidal mask. Hough Transform finds line segments. Features like slope and intercept are calculated to assign them to Left or Right groups. A 1D polyfit algorithm overlays solid lane lines."
    pdf.multi_cell(0, 6, impl)
    pdf.ln(10)
    
    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "9. Screenshots / Results", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 6, "Evaluation Results (Synthetic Test Set - 90 Images):", ln=True)
    pdf.cell(0, 6, "Left Lane Detection Rate: 87.0%", ln=True)
    pdf.cell(0, 6, "Right Lane Detection Rate: 71.0%", ln=True)
    pdf.cell(0, 6, "Overall Mean Absolute Error: 15.54 pixels", ln=True)
    pdf.ln(5)
    pdf.cell(0, 6, "Evaluation Results (Real-World Dashcam Data - 681 Frames):", ln=True)
    pdf.cell(0, 6, "Overall Tracking Yield: 100.0% coverage", ln=True)
    pdf.ln(5)
    pdf.cell(0, 6, "Below is a sample output generated from the evaluation.", ln=True)
    
    # --- PAGE 5 ---
    pdf.add_page()
    pdf.image("outputs/evaluated_test/frame_0300.jpg", x=30, w=150)
    pdf.ln(15)
    
    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "10. Testing Approach", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 6, "Pytest tests are included for preprocessing, lane detection, ROI processing, and the main pipeline. Running pytest returns 10 passed tests in 0.10s.")
    pdf.ln(10)
    
    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "11. Challenges Faced", ln=True)
    pdf.set_font("Arial", "", 11)
    chall_text = "The primary challenge was setting up a robust geometric filter for lines of varying slopes. Due to the lack of perfect visibility, a custom line separation algorithm had to be implemented from scratch in pure Python/NumPy. Additionally, tuning the Canny thresholds to correctly detect lane edges despite Gaussian noise required careful adjustment."
    pdf.multi_cell(0, 6, chall_text)
    pdf.ln(10)
    
    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "12. Learnings & Key Takeaways", ln=True)
    pdf.set_font("Arial", "", 11)
    learn = "I learned that classical CV techniques require careful tuning of parameters (like kernel size and threshold methods) to work effectively. I also learned that geometric engineering (like separating positive and negative slopes) is critical when relying on simpler linear modeling instead of deep learning feature extractors."
    pdf.multi_cell(0, 6, learn)
    
    # --- PAGE 6 ---
    pdf.add_page()
    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "13. Future Enhancements", ln=True)
    pdf.set_font("Arial", "", 11)
    future = "Future improvements could include implementing perspective transformation before Hough detection, which would likely increase accuracy by providing a bird's eye view. Additionally, implementing temporal smoothing or curve fitting could improve the robustness to heavy noise and winding roads."
    pdf.multi_cell(0, 6, future)
    pdf.ln(10)
    
    pdf.set_font("Arial", "BI", 20)
    pdf.cell(0, 12, "14. References", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 6, "1. OpenCV Documentation: https://docs.opencv.org/", ln=True)
    pdf.cell(0, 6, "2. Python NumPy Documentation: https://numpy.org/doc/", ln=True)
    
    pdf.output("Project_Report.pdf")

if __name__ == "__main__":
    create_report()
    print("Report built in root directory.")
