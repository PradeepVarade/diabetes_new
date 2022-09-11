import pickle
import json
import config
import numpy as np

class DiabetesData():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age
        
    def load_model(self) :
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model =pickle.load(f)
            
        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data =json.load(f)    
    
    def get_diabetes_prediction(self):
        self.load_model()
        test_array = np.zeros(len(self.json_data['columns']))
        
        test_array[0] = self.Glucose
        test_array[1] = self.BloodPressure
        test_array[2] = self.SkinThickness
        test_array[3] = self.Insulin
        test_array[4] = self.BMI
        test_array[5] = self.DiabetesPedigreeFunction
        test_array[6] = self.Age
        
        
        
        predicted_category = np.around(self.model.predict([test_array])[0],2)
        return predicted_category

            
    


