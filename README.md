# Baggage Security Scanning System with YOLOv8

![WhatsApp Görsel 2025-08-16 saat 20 53 08_d60eaa0a](https://github.com/user-attachments/assets/bfc64cc7-3c61-4dee-8e27-9d04b786d29d)


This project presents a web-based **Baggage Security Scanning System** designed to detect dangerous objects within X-ray images. The system leverages a state-of-the-art YOLOv8 object detection model served via a Flask API. Users can upload an X-ray image through a simple web interface, and the application will analyze it in real-time to identify and highlight potential threats.

## 🚀 Features

-   **Web-Based Interface:** An intuitive and user-friendly interface for uploading X-ray images and viewing detection results instantly.
-   **High-Accuracy Object Detection:** Utilizes a custom-trained YOLOv8 model to accurately detect contraband items.
-   **Real-Time Analysis:** Uploaded images are processed on the fly, with detected objects marked by bounding boxes and confidence scores.
-   **RESTful API:** The core detection logic is wrapped in a Flask API, making the model accessible as a service.
-   **Detailed Logging:** Keeps a record of detection events in both `.csv` and `.json` formats for tracking and analysis.

## 🛠️ Technologies & Libraries Used

This project integrates a range of libraries and frameworks, categorized by their function.

#### 1. Deep Learning / Model
-   **PyTorch:** The core deep learning framework used for running the YOLO model and enabling transfer learning.
-   **Ultralytics (YOLOv8):** The state-of-the-art object detection model architecture used for training and inference.
-   **torchvision:** Utilized for dataset transformations and accessing pretrained models.

#### 2. Image Processing
-   **OpenCV (`cv2`):** Applied for image preprocessing tasks such as noise reduction (Gaussian Blur, Median Filter) and edge detection (Canny, Sobel).
-   **Pillow (`PIL`):** Essential for opening, manipulating, and saving image files in various formats.
-   **matplotlib:** Used for visualizing images and drawing bounding boxes during development and debugging.
-   **NumPy:** The fundamental package for numerical and matrix operations on image data.

#### 3. Dataset & Annotation
-   **Roboflow:** Used for dataset management, annotation, and applying data augmentation techniques.
-   **pandas:** Employed for analyzing and processing annotation files (e.g., CSVs) during the data preparation phase.

#### 4. Model Serving & API
-   **Flask:** A lightweight web framework used to build the RESTful API that serves the YOLOv8 model.
-   **requests:** Used for testing the API endpoints during development.

#### 5. Additional Tools
-   **albumentations:** A powerful library for advanced data augmentation to improve model robustness.
-   **scikit-learn:** Used for evaluating model performance with metrics like precision, recall, and F1-score.

## 📂 Project Structure

The repository is organized as follows:

```
xray-nokta-tespiti/
├── app.py                  # Main Flask application file containing API endpoints
├── best.pt                 # Trained YOLOv8 model weights
├── logs.csv                # Log file for detections in CSV format
├── logs.json               # Log file for detections in JSON format
├── .gitignore              # Specifies files for Git to ignore
├── static/                 # Contains static assets like CSS and JavaScript
├── templates/              # HTML templates for the web interface (index.html, etc.)
└── uploads/                # Default directory for storing user-uploaded images

```

## 📦 Installation

Follow these steps to set up and run the project on your local machine.

**1. Clone the Repository:**
```bash
git clone https://github.com/tugcemukul/Luggage-Threat-Detection-System-Using-YOLOv8-and-Flask-API.git
cd xray-nokta-tespiti
```

**2. Create and Activate a Virtual Environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies:**
Install all the required Python libraries from a `requirements.txt` file.
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Once the installation is complete, start the Flask application with the following command:

```bash
python app.py
```

After the server starts, you will see output similar to this in your terminal:
```
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

Open your web browser and navigate to `http://127.0.0.1:5000`. You can now use the application to upload an X-ray image and see the detection results.
