# CS445 Final Project - Skin Cancer Classification
---
## Introduction
This is a web-based application for classifying skin cancer through images using a Convolutional Neural Network (CNN). Users could upload their skin lesions images and receive an immediate prediction of the disease type. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributors](#contributors)

## Installation
To set up the project locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/niconicoo0w0/CS445_FinalProject.git
   ```
2. Download the model:
   https://drive.google.com/file/d/1--9xSv2z0aDv_gpp5dZgOh9isyTAtxML/view?usp=sharing
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
## Usage
To run the application:
1. Navigate to the project directory.
2. Change the path for the model in app.py.
   ```bash
   model = tf.keras.models.load_model('replace/it/with/your/actual/path')
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open a web browser and go to `http://localhost:5000` to access the application.

## Features
- Users can upload images of skin lesions for analysis.
- The application provides real-time predictions with approximately 80% accuracy of the type of skin cancer.
- Provides links for further information on the predicted skin lesion type.

## Dependencies
- Python 3
- Flask
- TensorFlow
- Keras
- Pillow
- NumPy

## Contributors
- Kaiwen Ren (kaiwenr2@illinois.edu)
- Rui Zhou (ruizhou3@illinois.edu)
- Tong Li (tongli5@illinois.edu)
- Zhilan Wang (zhilanw2@illinois.edu)

