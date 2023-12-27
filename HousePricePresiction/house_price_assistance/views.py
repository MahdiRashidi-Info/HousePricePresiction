import pandas as pd
import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static  
from house_price_assistance.models import PredictPriceModel
import numpy as np
import joblib

file_path = os.path.join(settings.BASE_DIR, 'house_price_assistance', 'static', 'addresses.csv')
model_file_path = os.path.join(settings.BASE_DIR, 'house_price_assistance', 'static', 'knnr_model.joblib')
scaler_file_path = os.path.join(settings.BASE_DIR, 'house_price_assistance', 'static', 'scaler.joblib')

def examine_view(request):

    #for remove all data in table
    # PredictPriceModel.objects.all().delete()
    
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

def admin_dashboard(request):

    if request.method == 'POST':
        
        print(request.POST)

        state = request.POST.get('state')
        state_mapping_df = pd.read_csv(file_path)

        # Perform the transformation based on the mapping
        transformed_value = state_mapping_df[state_mapping_df['Original_Address'] == state]['Transformed_Value'].values
        area = request.POST.get('Area')

        facilities = request.POST.getlist('facility')
        rRoom = request.POST.get("Room")

        parking = 0
        warehouse = 0
        elevator = 0

        if 'parking' in facilities:
            parking = 1
        if 'warehouse' in facilities:
            warehouse = 1
        if 'elevator' in facilities:
            elevator = 1


        user_input = np.array([[area, rRoom, parking, warehouse, elevator, transformed_value[0]]])
        predicted_price = get_prediction(user_input)

        PredictPriceModel.objects.create(
            name=request.POST.get('nickName'),
            phone=request.POST.get('phone'),
            area=area,
            predict_price=predicted_price,
            room=rRoom,
            state=state,
            needParking = parking,
            needWareHouse = warehouse,
            needElevator = elevator,
        )
        
        all_rows = PredictPriceModel.objects.all()
        return render(request, 'result.html' , {'data' : all_rows})       
    #     return HttpResponse(predicted_price)
    # else:
    #     return HttpResponse('Not allowed to call!')
    