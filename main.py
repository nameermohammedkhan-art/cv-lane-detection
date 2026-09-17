import argparse
import os
import json
import cv2
from src.utils import load_image, save_image
from src.pipeline import process_image
from src.evaluation import evaluate_predictions

def run_detect(image_path, output_dir="outputs/detected"):
    try:
        img = load_image(image_path)
    except Exception as e:
        print(f"Error: {e}")
        return None
        
    out_img, left_lane, right_lane = process_image(img)
    
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.basename(image_path)
    out_path = os.path.join(output_dir, filename)
    
    save_image(out_path, out_img)
    
    print(f"Input: {image_path}")
    print(f"Left lane detected: {'yes' if left_lane else 'no'}")
    print(f"Right lane detected: {'yes' if right_lane else 'no'}")
    print(f"Output: {out_path}")
    
    return {"left": left_lane, "right": right_lane}

def run_batch_detect(input_dir, output_dir="outputs/detected"):
    if not os.path.exists(input_dir):
        print(f"Error: Directory not found: {input_dir}")
        return
        
    predictions = {}
    
    print(f"Running batch detection on {input_dir}...")
    for filename in os.listdir(input_dir):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            filepath = os.path.join(input_dir, filename)
            res = run_detect(filepath, output_dir)
            if res:
                predictions[filename] = res
                
    return predictions

def run_evaluate(data_dir="data", split="test"):
    img_dir = os.path.join(data_dir, split)
    labels_file = os.path.join(data_dir, f"{split}_labels.json")
    
    if not os.path.exists(img_dir):
        print(f"Error: Data directory '{img_dir}' not found.")
        return
        
    ground_truths = None
    if os.path.exists(labels_file):
        with open(labels_file, "r") as f:
            ground_truths = json.load(f)
    else:
        print(f"Warning: Labels file '{labels_file}' not found. Evaluating detection yield only.")
        
    predictions = run_batch_detect(img_dir, output_dir=f"outputs/evaluated_{split}")
    
    if not predictions:
        print("No predictions to evaluate.")
        return
        
    metrics = evaluate_predictions(predictions, ground_truths)
    
    os.makedirs("outputs", exist_ok=True)
    metrics_path = os.path.join("outputs", "metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)
        
    print(f"\nEvaluation Results:")
    print(f"Total Images: {metrics['total_images']}")
    print(f"Left Lane Detection Rate: {metrics['left_lane_detection_rate']:.2f}")
    print(f"Right Lane Detection Rate: {metrics['right_lane_detection_rate']:.2f}")
    print(f"Left Lane MAE: {metrics['left_lane_mae']:.2f}" if metrics['left_lane_mae'] else "Left Lane MAE: N/A")
    print(f"Right Lane MAE: {metrics['right_lane_mae']:.2f}" if metrics['right_lane_mae'] else "Right Lane MAE: N/A")
    print(f"Overall MAE: {metrics['overall_mae']:.2f}" if metrics['overall_mae'] else "Overall MAE: N/A")
    print(f"Metrics saved to {metrics_path}")

def main():
    parser = argparse.ArgumentParser(description="Road Lane Detection and Analysis System")
    parser.add_argument("--prepare-data", action="store_true", help="Generate synthetic dataset")
    parser.add_argument("--detect", type=str, help="Path to a single image for detection")
    parser.add_argument("--batch-detect", type=str, help="Path to a directory of images for batch detection")
    parser.add_argument("--evaluate", type=str, nargs='?', const="data", help="Evaluate the system on the test dataset. Provide path to data directory, defaults to 'data'")
    
    args = parser.parse_args()
    
    if args.prepare_data:
        os.system("python scripts/prepare_data.py --num 600")
    elif args.detect:
        run_detect(args.detect)
    elif args.batch_detect:
        run_batch_detect(args.batch_detect)
    elif args.evaluate:
        run_evaluate(data_dir=args.evaluate)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
