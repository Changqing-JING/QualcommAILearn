#!/usr/bin/env python3
"""
Postprocess EfficientNet-B0 output and show top-5 predictions
"""

import sys
import numpy as np
import urllib.request
import os

# ImageNet class labels URL
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
LABELS_FILE = "imagenet_classes.txt"

def load_imagenet_labels():
    """Download and load ImageNet class labels"""
    if not os.path.exists(LABELS_FILE):
        print(f"Downloading ImageNet labels...")
        urllib.request.urlretrieve(LABELS_URL, LABELS_FILE)
    
    with open(LABELS_FILE, 'r') as f:
        labels = [line.strip() for line in f.readlines()]
    return labels

def postprocess_output(output_path, top_k=5):
    """Load raw output and show top-k predictions"""
    # Load output (1000 float32 values)
    output = np.fromfile(output_path, dtype=np.float32)
    
    if len(output) != 1000:
        print(f"Warning: Expected 1000 values, got {len(output)}")
    
    # Apply softmax
    exp_output = np.exp(output - np.max(output))
    probs = exp_output / np.sum(exp_output)
    
    # Get top-k indices
    top_indices = np.argsort(probs)[::-1][:top_k]
    
    # Load labels
    labels = load_imagenet_labels()
    
    print(f"\n{'='*50}")
    print(f"Top {top_k} Predictions:")
    print(f"{'='*50}")
    
    for i, idx in enumerate(top_indices):
        label = labels[idx] if idx < len(labels) else f"Class {idx}"
        print(f"  {i+1}. {label}: {probs[idx]*100:.2f}%")
    
    print(f"{'='*50}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <output.raw>")
        print(f"  The output.raw is typically in ./output/Result_0/output.raw")
        sys.exit(1)
    
    postprocess_output(sys.argv[1])
