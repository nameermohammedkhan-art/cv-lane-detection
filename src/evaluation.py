import numpy as np

def calculate_lane_error(pred_lane, gt_lane):
    """Calculates the mean absolute error between predicted and ground truth lane coordinates."""
    if pred_lane is None or gt_lane is None:
        return None # Can't calculate error if one is missing
        
    pred = np.array(pred_lane, dtype=float)
    gt = np.array(gt_lane, dtype=float)
    
    # Calculate Mean Absolute Error (MAE) of endpoints
    mae = np.mean(np.abs(pred - gt))
    return mae

def evaluate_predictions(predictions, ground_truths):
    """
    Evaluates a set of predictions against ground truth data.
    predictions: dict of {filename: {"left": [x1,y1,x2,y2], "right": [x1,y1,x2,y2]}}
    ground_truths: dict of {filename: {"left": [x1,y1,x2,y2], "right": [x1,y1,x2,y2]}}
    """
    left_errors = []
    right_errors = []
    
    left_detected_count = 0
    right_detected_count = 0
    total_images = len(ground_truths)
    
    for filename, gt in ground_truths.items():
        if filename not in predictions:
            continue
            
        pred = predictions[filename]
        
        # Left lane
        if pred["left"] is not None:
            left_detected_count += 1
            if gt["left"] is not None:
                err = calculate_lane_error(pred["left"], gt["left"])
                if err is not None:
                    left_errors.append(err)
                    
        # Right lane
        if pred["right"] is not None:
            right_detected_count += 1
            if gt["right"] is not None:
                err = calculate_lane_error(pred["right"], gt["right"])
                if err is not None:
                    right_errors.append(err)
                    
    metrics = {
        "total_images": total_images,
        "left_lane_detection_rate": left_detected_count / total_images if total_images > 0 else 0,
        "right_lane_detection_rate": right_detected_count / total_images if total_images > 0 else 0,
        "left_lane_mae": np.mean(left_errors) if left_errors else None,
        "right_lane_mae": np.mean(right_errors) if right_errors else None,
        "overall_mae": np.mean(left_errors + right_errors) if (left_errors + right_errors) else None
    }
    
    return metrics
