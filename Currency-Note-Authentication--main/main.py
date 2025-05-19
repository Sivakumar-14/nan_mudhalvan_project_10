# Install OpenCV
# !pip install opencv-python opencv-contrib-python

# Import necessary libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the images: One genuine, one test
# Replace these paths with your uploaded file paths in Colab
genuine_img = cv2.imread('/content/genuine.jpg', 0)  
test_img = cv2.imread('/content/test.jpg', 0)        

# Initialize ORB detector
orb = cv2.ORB_create()

# Find keypoints and descriptors
kp1, des1 = orb.detectAndCompute(genuine_img, None)
kp2, des2 = orb.detectAndCompute(test_img, None)

# Create BFMatcher and match descriptors
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Sort matches by distance (lower distance is better)
matches = sorted(matches, key=lambda x: x.distance)

# Draw top 50 matches
img_matches = cv2.drawMatches(genuine_img, kp1, test_img, kp2, matches[:50], None, flags=2)

# Show results
plt.figure(figsize=(12,6))
plt.title('Feature Matches between Genuine and Test Notes')
plt.imshow(img_matches)
plt.axis('off')
plt.show()

# Basic similarity score: Ratio of good matches
good_matches = [m for m in matches if m.distance < 50]  # Threshold can be adjusted
similarity = len(good_matches) / len(matches) * 100
print(f"Similarity Score: {similarity:.2f}%")

# Make a simple decision
if similarity > 40:
    print("Likely Genuine")
else:
    print("Possibly Fake")
