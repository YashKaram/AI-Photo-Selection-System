# AI Photo Selection System

This project automatically selects the best photos from a group of images using Computer Vision techniques.

## Features

- Detects faces in images
- Identifies sharp and clear photos
- Removes blurred images
- Supports group photos, single photos and mixed photos
- Automatically selects the best images

## Technologies Used

- Python
- OpenCV
- MediaPipe
- Machine Learning
- Streamlit

## How to Run

1. Clone the repository

git clone https://github.com/YashKaram/AI-Photo-Selection.git

2. Install dependencies

pip install -r requirements.txt

3. Run the project

python app.py

## Project Type

Computer Vision + Artificial Intelligence

## 🏗 System Architecture

![Architecture](assets/architecture.png)

## 📂 Dataset

The system works with user-uploaded images.

Supported types:

- Single person photos
- Group photos
- Mixed image collections

The dataset used during testing contains:

- Portrait images
- Group event photos
- Multiple lighting conditions
- Different face orientations

Images are analyzed using computer vision techniques to determine the best quality photos.

## ⚙️ Model Workflow

1. Image Upload
Users upload multiple images.

2. Image Preprocessing
Images are resized and normalized.

3. Face Detection
MediaPipe detects faces in images.

4. Quality Analysis
The system checks:

- image sharpness
- face visibility
- brightness
- blur level

5. Photo Ranking
Images are scored based on quality.

6. Best Photo Selection
The system selects the highest scoring images.

## 🛠 Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy
- Streamlit
- Machine Learning
