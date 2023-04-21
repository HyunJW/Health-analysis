from flask import Flask, render_template, request
from keras.models import load_model
import numpy as np
import joblib

app = Flask(__name__)
@app.route('/', methods=['GET'])
def main():
    return render_template('diabetes/input.html')

@app.route('/result', methods=['POST'])
def result():
    model = load_model('C:/data/minitot/neo_keras.h5')
    scaler = joblib.load('C:/data/minitot/scaler.model')

    age = int(request.form['age'])
    sex = request.form['sex']
    try:
        chol = float(request.form['chol'])
    except:
        chol = 0
    chol_check = request.form['chol_check']
    BMI = float(request.form['BMI'])
    smoke = request.form['smoke']
    HDA = int(request.form['HDA'])
    PA = request.form['PA']
    fruit = request.form['fruit']
    veggies = request.form['veggies']
    HAC = request.form['HAC']
    GH = int(request.form['GH'])
    MH = int(request.form['MH'])
    PH = int(request.form['PH'])
    DW = request.form['DW']
    stroke = int(request.form['stroke'])
    HBP = request.form['HBP']

    age1 = 0
    age2 = 0
    age3 = 0
    age4 = 0
    age5 = 0
    age6 = 0
    age7 = 0
    age8 = 0
    age9 = 0
    age10 = 0
    age11 = 0
    age12 = 0
    age13 = 0

    if age < 25:
        age1 = 1
    elif age < 30:
        age2 = 1
    elif age < 35:
        age3 = 1
    elif age < 40:
        age4 = 1
    elif age < 45:
        age5 = 1
    elif age < 50:
        age6 = 1
    elif age < 55:
        age7 = 1
    elif age < 60:
        age8 = 1
    elif age < 65:
        age9 = 1
    elif age < 70:
        age10 = 1
    elif age < 75:
        age11 = 1
    elif age < 80:
        age12 = 1
    else:
        age13 = 1

    if sex == 'male':
        female = 0
        male = 1
    else:
        female = 1
        male = 0
    if np.isnan(chol):
        chol_check = 'no'
        chol = 0
    if float(chol) >= 240:
        chol0 = 0
        chol1 = 1
    else:
        chol0 = 1
        chol1 = 0
    if chol_check == 'yes':
        CC0 = 0
        CC1 = 1
    else:
        CC0 = 1
        CC1 = 0
    if smoke == 'yes':
        smoke0 = 0
        smoke1 = 1
    else:
        smoke0 = 1
        smoke1 = 0
    if HDA == 1:
        HDA0 = 0
        HDA1 = 1
    else:
        HDA0 = 1
        HDA1 = 0
    if PA == 'yes':
        PA0 = 0
        PA1 = 1
    else:
        PA0 = 1
        PA1 = 0
    if fruit == 'yes':
        fruit0 = 0
        fruit1 = 1
    else:
        fruit0 = 1
        fruit1 = 0
    if veggies == 'yes':
        veggie0 = 0
        veggie1 = 1
    else:
        veggie0 = 1
        veggie1 = 0
    if HAC == 'yes':
        drink0 = 0
        drink1 = 1
    else:
        drink0 = 1
        drink1 = 0

    for i in range(1, 6):
        globals()[f'health{i}'] = 0
        if GH == i:
            globals()[f'health{i}'] = 1

    if DW == 1:
        HW0 = 0
        HW1 = 1
    else:
        HW0 = 1
        HW1 = 0
    if stroke == 1:
        stroke0 = 0
        stroke1 = 1
    else:
        stroke0 = 1
        stroke1 = 0
    if HBP == 1:
        HBP0 = 0
        HBP1 = 1
    else:
        HBP0 = 1
        HBP1 = 0

    variables = [[BMI, MH, GH,
                  age1, age2, age3, age4, age5, age6, age7, age8, age9, age10, age11, age12, age13,
                  female, male,
                  chol0, chol1,
                  CC0, CC1,
                  smoke0, smoke1,
                  HDA0, HDA1,
                  PA0, PA1,
                  fruit0, fruit1,
                  veggie0, veggie1,
                  drink0, drink1,
                  health1, health2, health3, health4, health5,
                  HW0, HW1,
                  stroke0, stroke1,
                  HBP0, HBP1]]

    input = scaler.transform(variables)
    prob = model.predict(input)
    print(prob)
    predict = [1 if prob >= 0.5 else 0]

    if predict[0] == 1:
        result = '당뇨'
    else:
        result = '정상'

    return render_template('diabetes/result.html', prob=f'{100 * prob[0][0]:.2f}%', result=result,
                           age=age, sex=sex, chol=chol, chol_check=chol_check, BMI=BMI,
                           smoke=smoke, HDA=HDA, PA=PA, fruit=fruit, veggies=veggies,
                           HAC=HAC, GH=GH, MH=MH, PH=PH,DW=DW, stroke=stroke, HBP=HBP)

if __name__ == '__main__':
    app.run(port=8000, threaded=False)