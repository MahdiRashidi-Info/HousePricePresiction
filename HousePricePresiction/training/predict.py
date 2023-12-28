import numpy as np
import joblib

# Load the trained model
loaded_model = joblib.load('knnr_model.joblib')

# user input
user_input = np.array([[65.0, 2, 1, 1, 1, 156]])

# Load the scaler used during training
scaler = joblib.load('scaler.joblib')

# Transform user input using the loaded scaler
user_input_scaled = scaler.transform(user_input.astype(float))

# Make prediction using the loaded model
user_prediction = loaded_model.predict(user_input_scaled)

# Display the predicted price
formatted_rounded_prediction = "{:,.0f}".format(user_prediction[0][0])
print(f"Predicted price for user input: {formatted_rounded_prediction} USD")
