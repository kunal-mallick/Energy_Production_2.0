from flask import Flask,render_template
import pandas
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)