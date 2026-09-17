import os
import cv2
import numpy as np
import json
import argparse
import random

def generate_road_image(width=640, height=480, slope_var=0.5, bg_intensity=100, noise_std=10, blur_k=3):
    """Generates a synthetic road image with left and right lane markings."""
    # Background road
    img = np.ones((height, width, 3), dtype=np.uint8) * bg_intensity
    
    # Add random noise
    noise = np.random.normal(0, noise_std, img.shape).astype(np.uint8)
    img = cv2.add(img, noise)
    
    # Lane base parameters
    center_x = width // 2
    lane_width_bottom = int(width * 0.8)
    lane_width_top = int(width * 0.2)
    roi_top = int(height * 0.6)
    
    # Introduce variability
    offset_x = random.randint(-30, 30)
    left_slope_mod = random.uniform(1-slope_var, 1+slope_var)
    right_slope_mod = random.uniform(1-slope_var, 1+slope_var)
    
    # Left lane coordinates
    left_x_bottom = center_x - lane_width_bottom // 2 + offset_x
    left_x_top = int(center_x - (lane_width_top // 2) * left_slope_mod) + offset_x
    left_y_bottom = height
    left_y_top = roi_top
    
    # Right lane coordinates
    right_x_bottom = center_x + lane_width_bottom // 2 + offset_x
    right_x_top = int(center_x + (lane_width_top // 2) * right_slope_mod) + offset_x
    right_y_bottom = height
    right_y_top = roi_top
    
    # Draw lanes (white lines)
    color = (255, 255, 255)
    thickness = 8
    cv2.line(img, (left_x_bottom, left_y_bottom), (left_x_top, left_y_top), color, thickness)
    cv2.line(img, (right_x_bottom, right_y_bottom), (right_x_top, right_y_top), color, thickness)
    
    # Apply blur
    if blur_k > 0:
        if blur_k % 2 == 0:
            blur_k += 1
        img = cv2.GaussianBlur(img, (blur_k, blur_k), 0)
        
    ground_truth = {
        "left": [left_x_bottom, left_y_bottom, left_x_top, left_y_top],
        "right": [right_x_bottom, right_y_bottom, right_x_top, right_y_top]
    }
    
    return img, ground_truth

def main():
    parser = argparse.ArgumentParser(description="Generate synthetic road dataset.")
    parser.add_argument("--num", type=int, default=600, help="Number of images to generate")
    parser.add_argument("--output-dir", type=str, default="data", help="Output directory")
    args = parser.parse_args()
    
    random.seed(42)
    np.random.seed(42)
    
    splits = {"train": int(args.num * 0.7), "val": int(args.num * 0.15), "test": int(args.num * 0.15)}
    
    # Ensure splits sum to num by adding remainder to train
    remainder = args.num - sum(splits.values())
    splits["train"] += remainder
    
    metadata = {}
    
    img_idx = 0
    for split, count in splits.items():
        split_dir = os.path.join(args.output_dir, split)
        os.makedirs(split_dir, exist_ok=True)
        
        metadata[split] = {}
        
        for _ in range(count):
            filename = f"image_{img_idx:04d}.png"
            filepath = os.path.join(split_dir, filename)
            
            # Vary generation parameters slightly
            slope_var = random.uniform(0.1, 0.4)
            bg_intensity = random.randint(80, 150)
            noise_std = random.randint(5, 20)
            blur_k = random.choice([3, 5, 7])
            
            img, gt = generate_road_image(slope_var=slope_var, bg_intensity=bg_intensity, noise_std=noise_std, blur_k=blur_k)
            cv2.imwrite(filepath, img)
            
            metadata[split][filename] = gt
            img_idx += 1
            
        # Save split metadata
        with open(os.path.join(args.output_dir, f"{split}_labels.json"), "w") as f:
            json.dump(metadata[split], f, indent=4)
            
    print(f"Successfully generated {args.num} images in {args.output_dir}")

if __name__ == "__main__":
    main()
