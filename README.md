
# House Price Prediction Web Application

## Overview
This project is a web application built with Django that utilizes K-Nearest Neighbors (KNN) algorithms to predict house prices (Tehran, Iran). The application allows users to input various features related to a house, and it provides a predicted price based on the KNN model.

## Features
- User-Friendly Interface: The web application provides an intuitive interface for users to input information about a house.
  
- KNN Prediction: The core of the prediction is powered by the K-Nearest Neighbors algorithm, trained on a dataset of historical house prices.
  
- Scalability: The project is designed to handle a growing dataset, and the KNN model can be updated as new data becomes available.

## Installation
To run this project locally, follow these steps:

1- Clone the repository:
```
https://github.com/MahdiRashidi-Info/HousePriceAssistance.git
cd HousePriceAssistance/MabaheshVizheProject
```

2- Install dependencies:
```
pip install -r requirements.txt
```

3- Apply database migrations:
```
python manage.py makemigrations
python manage.py migrate
```

4- Run the development server:
```
python manage.py runserver
```

## Usage
1- Input the relevant features of the house into the web application.

2- Click the "Predict" button to get the predicted house price.

3- See the price of the house in your panel.

## Dataset
Link: https://www.kaggle.com/datasets/mokar2001/house-price-tehran-iran


