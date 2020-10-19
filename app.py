from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('heart.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("heart_prediction.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    #Age
    data1 = request.form['a']
    if data1 == "":
        data1 = 40
    else:
        data1 = request.form['a']

    #Gender
    data2 = request.form['b']
    if data2 =="m" or data2 == "M":
        data2 = 0
    else:
        data2 = 1
        print(data2)
    # Chest Pain
    data3 = request.form['c']
    if data3 == "":
        data3 = 0
    else:
        data3 = request.form['c']

    # Resting Blood pressure
    data4 = request.form['d']
    if data4 == "":
        data4 = 100
    else:
        data4 = request.form['d']

    # Cholesterol
    data5 = request.form['e']
    if data5 == "":
        data5 = 200
    else:
        data5 = request.form['e']

    # Fasting blood pressure
    data6 = request.form['f']
    if data6 == "":
        data6 = 0
    else:
        data6 = request.form['f']

    # Resting ECG
    data7 = request.form['g']
    if data7 == "":
        data7 = 0
    else:
        data7 = request.form['g']

    # Maximum Heart rate
    data8 = request.form['h']
    if data8 == "":
        data8 = 170
    else:
        data8 = request.form['h']

    # Exercise induced angina
    data9 = request.form['i']
    if data9 == "":
        data9 = 0
    else:
        data9 = request.form['i']

    arr = np.array([[data1, data2, data3,data4, data5, data6, data7, data8,data9]])
    prediction = model.predict(arr)

    output = prediction

    if output == 1:
        return render_template('high_risk.html', pred='High Risk of Heart Disease {}'.format(output))
    else:
        return render_template('low_risk.html', pred='Low Risk of Heart Disease {}'.format(output))



if __name__ == '__main__':
    app.run(debug=True)