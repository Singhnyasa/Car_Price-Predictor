import self as self
from flask import Flask,render_template,request,redirect

import pickle
import pandas as pd
import numpy as np

app=Flask(__name__,template_folder='template')

model = pickle.load(open('C:/Users/Nyasa/PycharmProjects/CarPredictor/LinearRegressionModel.pkl','rb'))
car=pd.read_csv('C:\\Users\\Nyasa\\PycharmProjects\\CarPredictor\\Cleaned_car.csv')

@app.route('/',methods=['GET','POST'])
def index():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=car['fuel_type'].unique()

    companies.insert(0,'Select Company')
    return render_template('index.html',companies=companies, car_models=car_models, years=year,fuel_types=fuel_type)


@app.route('/predict',methods=['POST'])

def predict():

    company=request.form.get('company')

    car_model=request.form.get('car_models')
    year=int(request.form.get('year'))
    fuel_type=request.form.get('fuel_type')
    driven=request.form.get('kilo_driven')

    prediction=model.predict(pd.DataFrame([[company, car_model, year, fuel_type, driven]],
                                        columns=['company', 'name', 'year', 'fuel_type','kms_driven']))
    print(prediction)

    return str(prediction[0])



if __name__=='__main__':
    app.run(debug =True)