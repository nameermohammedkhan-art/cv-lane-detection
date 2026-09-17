import cv2
import numpy as np

def draw_rect_with_text(img, text, pt1, pt2, color=(173, 216, 230), font_scale=0.5):
    cv2.rectangle(img, pt1, pt2, color, -1)
    cv2.rectangle(img, pt1, pt2, (0,0,0), 1)
    
    # Text size
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 1)[0]
    text_x = pt1[0] + (pt2[0] - pt1[0] - text_size[0]) // 2
    text_y = pt1[1] + (pt2[1] - pt1[1] + text_size[1]) // 2
    cv2.putText(img, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0,0,0), 1)

def generate_arch():
    img = np.ones((100, 600, 3), dtype=np.uint8) * 255
    steps = ["Input", "Gray & Blur", "Canny", "ROI", "Hough", "Output"]
    for i, s in enumerate(steps):
        pt1 = (20 + i*90, 30)
        pt2 = (90 + i*90, 70)
        draw_rect_with_text(img, s, pt1, pt2, font_scale=0.4)
        if i < len(steps)-1:
            cv2.arrowedLine(img, (90 + i*90, 50), (20 + (i+1)*90, 50), (0,0,0), 1, tipLength=0.3)
    cv2.imwrite("docs/arch.png", img)

def generate_workflow():
    img = np.ones((400, 200, 3), dtype=np.uint8) * 255
    steps = ["Start", "Process Image", "Extract Lanes", "Predict Lines", "End"]
    for i, s in enumerate(steps):
        pt1 = (50, 20 + i*70)
        pt2 = (150, 60 + i*70)
        draw_rect_with_text(img, s, pt1, pt2, font_scale=0.4)
        if i < len(steps)-1:
            cv2.arrowedLine(img, (100, 60 + i*70), (100, 20 + (i+1)*70), (0,0,0), 1)
    cv2.imwrite("docs/flow.png", img)

def generate_usecase():
    img = np.ones((200, 400, 3), dtype=np.uint8) * 255
    cv2.putText(img, "User", (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)
    cases = ["Prepare Data", "Train / Detect", "Test System", "Predict Image"]
    for i, c in enumerate(cases):
        pt1 = (150, 20 + i*40)
        pt2 = (300, 50 + i*40)
        cv2.ellipse(img, (225, 35 + i*40), (75, 15), 0, 0, 360, (0,0,0), 1)
        text_size = cv2.getTextSize(c, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 1)[0]
        cv2.putText(img, c, (225 - text_size[0]//2, 35 + i*40 + text_size[1]//2), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 1)
        cv2.line(img, (70, 100), (150, 35 + i*40), (0,0,0), 1)
    cv2.imwrite("docs/usecase.png", img)

def generate_class():
    img = np.ones((200, 400, 3), dtype=np.uint8) * 255
    pt1 = (100, 20)
    pt2 = (300, 180)
    cv2.rectangle(img, pt1, pt2, (0,0,0), 1)
    cv2.line(img, (100, 50), (300, 50), (0,0,0), 1)
    cv2.putText(img, "LaneDetector", (150, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)
    cv2.putText(img, "+ detect()", (110, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 1)
    cv2.putText(img, "+ evaluate()", (110, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 1)
    cv2.putText(img, "+ draw()", (110, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 1)
    cv2.imwrite("docs/class.png", img)

if __name__ == "__main__":
    generate_arch()
    generate_workflow()
    generate_usecase()
    generate_class()
    print("Diagrams done.")
