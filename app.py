import pickle
import math as mt
import numpy as np
from flask import Flask,render_template, request

app=Flask(__name__)

load = open('model.pkl','rb')
model = pickle.load(load)

@app.route('/')
def welcome():
    return render_template('index.html', r1='Check Your', r2='Energy', r3 = ' Production')

@app.post('/')
def pre():
    temp = mt.log(float(request.form["temp"]))
    ev = float(request.form["ev"])
    ap = mt.log(float(request.form["ap"]))
    prediction = model.predict([[temp, ev, ap]])
    predict = round(prediction[0],2)
    return render_template('index.html', r1='Energy Product is', r2='{}'.format(predict), r3 = ' mw')

if __name__=='__main__':
    app.run()