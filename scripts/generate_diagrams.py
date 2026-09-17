import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import numpy as np

def draw_architecture():
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.axis('off')
    
    steps = ["Input Image", "Grayscale", "Gaussian Blur", "Canny Edge", "ROI Mask", "Hough Lines", "Separation", "Output"]
    
    for i, step in enumerate(steps):
        rect = patches.Rectangle((i*1.2, 0), 1, 0.5, linewidth=1, edgecolor='black', facecolor='lightblue')
        ax.add_patch(rect)
        ax.text(i*1.2 + 0.5, 0.25, step, ha='center', va='center', fontsize=8, wrap=True)
        
        if i < len(steps) - 1:
            ax.arrow(i*1.2 + 1, 0.25, 0.15, 0, head_width=0.05, head_length=0.05, fc='k', ec='k')
            
    ax.set_xlim(-0.2, len(steps)*1.2)
    ax.set_ylim(-0.5, 1)
    plt.savefig("docs/architecture.png", bbox_inches='tight', dpi=300)
    plt.close()

def draw_workflow():
    fig, ax = plt.subplots(figsize=(4, 6))
    ax.axis('off')
    
    steps = ["Start", "Generate Data", "Process Image", "Extract Lanes", "Evaluate", "End"]
    for i, step in enumerate(steps):
        y = 5 - i
        rect = patches.Rectangle((1, y), 2, 0.6, linewidth=1, edgecolor='black', facecolor='lightblue')
        ax.add_patch(rect)
        ax.text(2, y + 0.3, step, ha='center', va='center')
        
        if i < len(steps) - 1:
            ax.arrow(2, y, 0, -0.3, head_width=0.1, head_length=0.1, fc='k', ec='k')
            
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 6)
    plt.savefig("docs/workflow.png", bbox_inches='tight', dpi=300)
    plt.close()

def draw_usecase():
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off')
    
    ax.text(1, 2, "User", ha='center', va='center')
    
    cases = ["Generate Data", "Detect Single", "Batch Detect", "Evaluate", "Test"]
    for i, case in enumerate(cases):
        y = 3.5 - i*0.8
        ellipse = patches.Ellipse((4, y), 2.5, 0.6, linewidth=1, edgecolor='black', facecolor='white')
        ax.add_patch(ellipse)
        ax.text(4, y, case, ha='center', va='center')
        ax.plot([1.3, 2.7], [2, y], 'k-', linewidth=1)
        
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 4)
    plt.savefig("docs/usecase.png", bbox_inches='tight', dpi=300)
    plt.close()
    
def draw_class():
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off')
    
    # Just a simple rectangle with text
    rect = patches.Rectangle((1, 1), 4, 2, linewidth=1, edgecolor='black', facecolor='white')
    ax.add_patch(rect)
    ax.plot([1, 5], [2.5, 2.5], 'k-')
    ax.text(3, 2.75, "LaneDetector", ha='center', va='center', fontweight='bold')
    ax.text(1.2, 1.8, "+ process_image(img)\n+ detect_lines(img)\n+ draw_lanes(img)\n+ evaluate()", va='center')
    
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 4)
    plt.savefig("docs/class.png", bbox_inches='tight', dpi=300)
    plt.close()

if __name__ == "__main__":
    draw_architecture()
    draw_workflow()
    draw_usecase()
    draw_class()
    print("Diagrams generated.")
