import pandas as pd
import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static  # Import the static template tag

import numpy as np
import joblib


file_path = os.path.join(settings.BASE_DIR, 'house_price_assistance', 'static', 'addresses.csv')
model_file_path = os.path.join(settings.BASE_DIR, 'house_price_assistance', 'static', 'knnr_model.joblib')
scaler_file_path = os.path.join(settings.BASE_DIR, 'house_price_assistance', 'static', 'scaler.joblib')

def examine_view(request):

    df = pd.read_csv(file_path)      
    original_addresses = df['Original_Address'].tolist()
    return render(request, 'main_form.html' ,{'city' : original_addresses})



# Load the trained model
loaded_model = joblib.load(model_file_path)

# Load the scaler used during training
scaler = joblib.load(scaler_file_path)

def get_prediction(user_input):
    # Transform user input using the loaded scaler
    user_input_scaled = scaler.transform(user_input.astype(float))
    
    # Make prediction using the loaded model
    user_prediction = loaded_model.predict(user_input_scaled)
    
    # Display the predicted price
    formatted_rounded_prediction = "{:,.0f}".format(user_prediction[0][0])
    
    return formatted_rounded_prediction

def form_submit_view(request):

    if request.method == 'POST':
        print(request.POST)
        
        state = request.POST.get('state')
        state_mapping_df = pd.read_csv(file_path)

        # Perform the transformation based on the mapping
        transformed_value = state_mapping_df[state_mapping_df['Original_Address'] == state]['Transformed_Value'].values
        area = request.POST.get('Area')

        facilities = request.POST.getlist('facility')


        parking = 0
        warehouse = 0
        elevator = 0
        room = 1

        if 'parking' in facilities:
            parking = 1
        if 'warehouse' in facilities:
            warehouse = 1
        if 'elevator' in facilities:
            elevator = 1


        user_input = np.array([[area, room, parking, warehouse, elevator, transformed_value[0]]])
        predicted_price = get_prediction(user_input)

        
        return HttpResponse(predicted_price)
    else:
        return HttpResponse('Not allowed to call!')
    