import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

from google.colab import files
uploaded = files.upload()

import pandas as pd

df = pd.read_csv('hand_sign_landmarks.csv')  # Change this to your file name
X = df.iloc[:, :-1]  # Landmark features
y = df.iloc[:, -1]   # Labels

# Convert the target variable to discrete if it's continuous
# Assuming 'label' column contains numerical values representing classes
# Replace this with appropriate conversion logic if needed
# For example, if your labels are continuous but represent categories:
# y = pd.cut(y, bins=[-float('inf'), 0, 1, float('inf')], labels=['class1', 'class2', 'class3'])

# Or, if you need to convert continuous values to integers:
from sklearn.preprocessing import LabelEncoder  # Import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)  # Convert continuous labels to integers

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

def extract_landmarks(results):
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        return np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]).flatten()
    return None

# NOTE: In Colab we cannot use a webcam directly. Use a video or image for testing.
cap = cv2.VideoCapture('sign.mp4')  # Upload this file or replace with your video

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        landmarks = extract_landmarks(results)
        if landmarks is not None:
            prediction = knn.predict([landmarks])
            cv2.putText(image, f"Sign: {prediction[0]}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    image = cv2.resize(image, (640, 480))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
