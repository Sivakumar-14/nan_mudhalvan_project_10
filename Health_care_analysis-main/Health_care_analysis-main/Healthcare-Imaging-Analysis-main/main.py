# Step 1: Install dependencies
# !pip install matplotlib

# Step 2: Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Step 3: Upload an X-ray image
uploaded = files.upload()

# Step 4: Load and process the image
for file_name in uploaded.keys():
    # Read in grayscale
    img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (512, 512))

    # Preprocess: blur and detect edges
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Convert to color for annotation
    annotated_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # Find the largest contour by area
    max_area = 0
    max_bbox = None
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h
        if area > max_area:
            max_area = area
            max_bbox = (x, y, w, h)

    # Draw a green rectangle if a significant contour was found
    if max_bbox and max_area > 100:  # Area threshold to avoid noise
        x, y, w, h = max_bbox
        cv2.rectangle(annotated_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the original and annotated image
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original X-ray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB))
    plt.title('Detected Fracture (Largest Region)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
