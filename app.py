import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load trained model and encoder
model = joblib.load("activity_model.pkl")
enconder = joblib.load("label_encoder.pkl")

st.title("Human Activity Recognition Agent")

st.write("Upload sensor data CSV file to predict activities.")

uploaded_file = st.file_uploader("Choose CSV File", type=["csv"])

activity_log = []

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.write(data.head())

    predictions = model.predict(data)

    activities = enconder.inverse_transform(predictions)

    data["Predicted Activity"] = activities

    st.subheader("Prediction Results")
    st.write(data)

    st.subheader("Activity Summary")

    for activity in activities:

        summary_dict = {
            "WALKING": "User is walking.",
            "WALKING_UPSTAIRS": "User is climbing upstairs.",
            "WALKING_DOWNSTAIRS": "User is moving downstairs.",
            "SITTING": "User is sitting.",
            "STANDING": "User is standing.",
            "LAYING": "User is resting."
        }

        summary = summary_dict.get(activity, "Unknown activity.")

        timestamp = datetime.now()

        activity_log.append({"Time": timestamp, "Activity": activity})

        st.write(f"{timestamp} → {activity} : {summary}")

    report = pd.DataFrame(activity_log)

    st.subheader("Activity Report")

    st.write(report["Activity"].value_counts())

    csv = data.to_csv(index=False)

    st.download_button(
        label="Download Results",
        data=csv,
        file_name="activity_predictions.csv",
        mime="text/csv"
    )
