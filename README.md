# Bank Authentication ML Model using FastAPI
This project implements a bank authentication machine learning model using the scikit-learn Random Forest Classifier. The model is trained on a dataset using train-test split, and the accuracy score is used to evaluate its performance. The trained model is then deployed using FastAPI, providing an API endpoint for authentication.

## Project Topic:
Bank Authentication ML Model with FastAPI Deployment

## Overview:
This repository contains the code for a bank authentication machine learning model, built using scikit-learn's Random Forest Classifier. The model is trained on a dataset containing features relevant to bank authentication. After training and evaluation using train-test split and accuracy score, the model is deployed using FastAPI, providing a simple and efficient API for authentication tasks.

## Project Structure:
model_training.ipynb: Jupyter Notebook containing the code for training the machine learning model.
app.py: Python script for deploying the trained model using FastAPI.
requirements.txt: File listing the dependencies required to run the project.
README.md: This file, providing an overview and instructions for the project.
# Usage Instructions:
Clone the Repository:
bash
Copy code
git clone <repository_url>
cd <repository_name>

## Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Train the Model:
Open and execute the model_training.ipynb notebook to train the Random Forest Classifier model using your dataset.
Deploy the Model with FastAPI:
Run the FastAPI application using the following command:
bash
Copy code
uvicorn app:app --reload
This command starts the FastAPI server, making the model accessible via HTTP endpoints.
## Authentication Requests:
Send POST requests to http://localhost:8000/predict with the required input data for authentication.
The model will respond with the authentication result.
## Note:
Ensure that the necessary data preprocessing steps are performed before training the model.
For deployment in production environments, consider using appropriate security measures and scaling strategies.

## Conclusion:
This project demonstrates the implementation of a bank authentication machine learning model using scikit-learn and its deployment as an API using FastAPI. For further enhancements or modifications, feel free to explore the code and adapt it to your specific requirements.

## Contact Information:
For inquiries or feedback, please contact: ugofebe@gmail.com
