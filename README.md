# human-activity-recognition-agent
Human Activity Recognition Agent
Problem Statement

Human Activity Recognition (HAR) is the process of identifying and classifying human physical activities using data collected from smartphone sensors such as accelerometers and gyroscopes. Accurate recognition of activities can be useful in healthcare monitoring, fitness tracking, elderly care, and smart living applications.

The objective of this project is to develop a Human Activity Recognition Agent that can automatically recognize activities performed by a user based on sensor data collected from smartphones.

Phase 1: Machine Learning Model

In this phase, a machine learning model is trained using the Human Activity Recognition dataset. Various classification algorithms such as:

Random Forest
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN)
XGBoost
Multi-Layer Perceptron (MLP)

can be used to classify human activities. The model is evaluated using performance metrics including:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix

The best-performing model is selected and saved for deployment.

Phase 2: AI Agent

In this phase, an intelligent Human Activity Recognition Agent is developed. The agent:

Accepts smartphone sensor readings as input.
Uses the trained machine learning model to predict user activities.
Generates activity summaries in human-readable format.
Maintains activity logs with timestamps.
Produces activity reports and statistics.
Monitors user behavior and detects inactivity patterns.
Activities Recognized

The system identifies the following activities:

WALKING
WALKING_UPSTAIRS
WALKING_DOWNSTAIRS
SITTING
STANDING
LAYING
Dataset

Dataset Used:
Human Activity Recognition Using Smartphones Dataset (Kaggle)

Technologies Used
Python
Pandas
NumPy
Scikit-Learn
Joblib
Streamlit
Matplotlib
Expected Outcome

The developed Human Activity Recognition Agent can accurately recognize user activities from smartphone sensor data, provide real-time activity monitoring, generate summaries and reports, and serve as a foundation for smart healthcare and fitness applications.
