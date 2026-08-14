import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask,render_template,jsonify,request

application=Flask(__name__)
app=application

#import models
linear_model=pickle.load(open("projects\End-to_end_p1\models\Linear.pkl","rb"))
scaler_model=pickle.load(open("projects\End-to_end_p1\models\scaler.pkl","rb"))

#render
@app.route("/")
def index():
    return render_template("index.html")
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=="POST":
        Temprature=float(request.form.get("Temprature"))
        RH=float(request.form.get("RH"))
        Ws=float(request.form.get("Ws"))
        Rain=float(request.form.get("Rain"))
        FFMC=float(request.form.get("FFMC"))
        DMC=float(request.form.get("DMC"))
        ISI=float(request.form.get("ISI"))
        
        new_scaled_data=scaler_model.transform([[Temprature, RH, Ws, Rain, FFMC, DMC, ISI]])
        predict_val=linear_model.predict(new_scaled_data)

        return render_template("home.html",result=predict_val[0])

    else:
        return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")