from flask import Flask,render_template, request
app=Flask(__name__)
import numpy as np

@app.route('/')
def welcome():
    return render_template('index.html', r1='Check Your', r2='Energy', r3 = ' Production')

@app.route('/pre', methods=['POST'])
def pre():
    temp = float(request.form["temp"])
    ev = float(request.form["ev"])
    ap = float(request.form["ap"])
    avg = (temp+ev+ap)/2
    return render_template('index.html', r1='Energy Product is', r2='{}'.format(avg), r3 = ' mw')

if __name__=='__main__':
    app.run(debug=True)