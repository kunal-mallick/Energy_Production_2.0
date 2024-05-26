from flask import Flask,render_template, request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# @app.route('/pre', methods=['POST'])
# def predict():
#     temp = request.form["temp"]
#     ev = request.form["ev"]
#     ap = request.form["ap"]
#     avg = (temp+ev+ap)/2
#     return render_template('index.html', result =''.format(avg))

if __name__=='__main__':
    app.run(debug=True)