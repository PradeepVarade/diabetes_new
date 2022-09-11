import re
from flask import Flask,jsonify,request
from project_app.utils import DiabetesData
import config

app=Flask(__name__)

@app.route('/')
def home_api():
    return "Welcome to Medical data Prediction"


@app.route('/predict_dia')
def get_patient_details():
    data = request.form 
    
    
    Glucose = eval(data['Glucose'])
    BloodPressure = eval(data['BloodPressure'])
    SkinThickness = eval(data['SkinThickness'])
    Insulin = eval(data['Insulin'])
    BMI = eval(data['BMI'])
    DiabetesPedigreeFunction = eval(data['DiabetesPedigreeFunction'])
    Age = eval(data['Age'])
    
    diesease_p = DiabetesData(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    predict=diesease_p.get_diabetes_prediction()
    return jsonify({"Patient diabetes evaluation =":f"{predict}"})    
    
if __name__=='__main__':
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=False)
    
    
    
    
    
