#!/usr/bin/env python3
"""
Preprocess image for EfficientNet-B0 inference with QNN
Converts image to raw float32 format expected by the model
"""

import sys
import numpy as np
from PIL import Image

def preprocess_for_efficientnet(image_path, output_path):
    """
    Preprocess image for EfficientNet-B0:
    - Resize to 256 (shorter edge)
    - Center crop to 224x224
    - Convert to RGB
    - Normalize with ImageNet mean/std
    - Save as raw float32
    """
    # Load image
    img = Image.open(image_path).convert('RGB')
    
    # Resize so shorter edge is 256 (preserve aspect ratio)
    w, h = img.size
    if w < h:
        new_w = 256
        new_h = int(h * 256 / w)
    else:
        new_h = 256
        new_w = int(w * 256 / h)
    img = img.resize((new_w, new_h), Image.BICUBIC)
    
    # Center crop to 224x224
    w, h = img.size
    left = (w - 224) // 2
    top = (h - 224) // 2
    img = img.crop((left, top, left + 224, top + 224))
    
    # Convert to numpy array and normalize to [0, 1]
    # Note: qai_hub_models EfficientNet has normalization built into the model
    # so we only scale to [0, 1], no ImageNet mean/std normalization
    img_array = np.array(img, dtype=np.float32) / 255.0
    
    # Model expects NCHW format: [1, 3, 224, 224]
    # Current shape is [224, 224, 3] (HWC)
    img_array = np.transpose(img_array, (2, 0, 1))  # HWC -> CHW
    img_array = np.expand_dims(img_array, axis=0)   # CHW -> NCHW
    
    # Ensure contiguous and save as raw binary
    img_array = np.ascontiguousarray(img_array, dtype=np.float32)
    img_array.tofile(output_path)
    
    print(f"Input image: {image_path}")
    print(f"Output raw file: {output_path}")
    print(f"Shape: {img_array.shape}")
    print(f"Dtype: {img_array.dtype}")
    print(f"Size: {img_array.nbytes} bytes")
    
    return output_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <image.jpg> [output.raw]")
        sys.exit(1)
    
    image_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else image_path.rsplit('.', 1)[0] + '.raw'
    
    preprocess_for_efficientnet(image_path, output_path)
