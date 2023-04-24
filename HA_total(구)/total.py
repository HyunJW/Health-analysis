from flask import Flask, render_template, request, redirect
import joblib
from keras.models import load_model
import numpy as np

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('total/mainpage.html')

@app.route('/menu1')
def menu1():
    return redirect('http://www.naver.com')

@app.route('/menu2')
def menu2():
    return redirect('http://www.daum.net')

@app.route('/menu3')
def menu3():
    return redirect('http://www.nate.com')

@app.route('/menu4')
def menu4():
    return redirect('http://www.google.go.kr')

@app.route('/menu5')
def menu5():
    return redirect('http://www.youtube.com')

@app.route('/heartattack', methods=['GET'])
def heartattack():
    return render_template('heartattack/input.html')

@app.route('/stroke', methods=['GET'])
def stroke():
    return render_template('stroke/input.html')

@app.route('/hypertension', methods=['GET'])
def hypertension():
    return render_template('hypertension/input.html')

@app.route('/diabetes', methods=['GET'])
def diabetes():
    return render_template('diabetes/input.html')

@app.route('/heartattack_result',methods=['POST'])
def heartattack_result():
    model = joblib.load('C:/Health Analysis/HA_total/heart_model.h5')
    scaler = joblib.load('C:/Health Analysis/HA_total/heart.sav')

    age = float(request.form['age'])
    trtbps = float(request.form['trtbps'])
    thalach = float(request.form['thalach'])
    oldspeak = float(request.form['oldspeak'])
    sex = request.form['sex']
    if sex == "f":
        female = 1
        male = 0
    else:
        female = 0
        male = 1
    cp = request.form['cp']
    if cp == "n":
        cp_n = 1
        cp_y = 0
    else:
        cp_n = 0
        cp_y = 1
    fbs = float(request.form['fbs'])
    if fbs <= 120:
        fbs_n = 1
        fbs_y = 0
    else:
        fbs_n = 0
        fbs_y = 1
    ecg = request.form['ecg']
    if ecg == "n":
        ecg_n = 1
        ecg_y = 0
    else:
        ecg_n = 0
        ecg_y = 1
    exang = request.form['exang']
    if exang == "n":
        exang_n = 1
        exang_y = 0
    else:
        exang_n = 0
        exang_y = 1
    sl = request.form['sl']
    if sl == "n":
        sl_n = 1
        sl_y = 0
    else:
        sl_n = 0
        sl_y = 1
    ca = request.form['ca']
    if ca == "n":
        ca_n = 1
        ca_y = 0
    else:
        ca_n = 0
        ca_y = 1
    test_set = [[age, trtbps, thalach, oldspeak,
                 female, male, cp_n, cp_y, fbs_n, fbs_y,
                 ecg_n, ecg_y, exang_n, exang_y, sl_n, sl_y,
                 ca_n, ca_y]]
    test_set = scaler.transform(test_set)
    pred = round(model.predict_proba(test_set)[0][1]*100,2)

    if pred >= 50:
        result = '심장마비 가능성 많음'
    else:
        result = '심장마비 가능성 적음'

    #pred=pred[0]*100

    return render_template('heartattack/result.html',
                           result=result, age=age, trtbps=trtbps,
                           thalach=thalach, oldspeak=oldspeak,
                           sex=sex, cp=cp, fbs=fbs, ecg=ecg, exang=exang,
                           sl=sl, ca=ca, pred=pred)

import tensorflow as tf
@app.route('/stroke_result',methods=['POST'])
def stroke_result():
    print(333)
    print(444)
    #kerasmodel = load_model('c:/Health Analysis/HA_total/test4/miniproject1.h5')
    kerasmodel = tf.keras.models.load_model('c:/Health Analysis/HA_total/miniproject1.h5', compile=False)

    scaler = joblib.load('c:/Health Analysis/HA_total/miniscaler.sav')
    SEX = request.form['SEX']
    AGE = float(request.form['AGE'])
    HYPERTENSION = request.form['HYPERTENSION']
    HEART_DISEASE = request.form['HEART_DISEASE']
    WORK_TYPE = request.form['WORK_TYPE']
    RESIDENCE_TYPE = request.form['RESIDENCE_TYPE']
    AVG_GLUCOSE_LEVEL = float(request.form['AVG_GLUCOSE_LEVEL'])
    BMI = float(request.form['BMI'])
    SMOKING_STATUS = request.form['SMOKING_STATUS']

    if SEX == '1':
        SEX_T = 1
        SEX_F = 0
    else:
        SEX_T = 0
        SEX_F = 1

    if HYPERTENSION == '1':
        HYPERTENSION_T = 1
        HYPERTENSION_F = 0
    else:
        HYPERTENSION_T = 0
        HYPERTENSION_F = 1
    if HEART_DISEASE =='1':
        HEART_DISEASE_T = 1
        HEART_DISEASE_F = 0
    else:
        HEART_DISEASE_T = 0
        HEART_DISEASE_F = 1

    if WORK_TYPE =='0':
        WORK_TYPE_0 = 1
        WORK_TYPE_1 = 0
        WORK_TYPE_2 = 0
        WORK_TYPE_3 = 0
        WORK_TYPE_4 = 0

    if WORK_TYPE =='1':
        WORK_TYPE_0 = 0
        WORK_TYPE_1 = 1
        WORK_TYPE_2 = 0
        WORK_TYPE_3 = 0
        WORK_TYPE_4 = 0

    if WORK_TYPE =='2':
        WORK_TYPE_0 = 0
        WORK_TYPE_1 = 0
        WORK_TYPE_2 = 1
        WORK_TYPE_3 = 0
        WORK_TYPE_4 = 0

    if WORK_TYPE =='3':
        WORK_TYPE_0 = 0
        WORK_TYPE_1 = 0
        WORK_TYPE_2 = 0
        WORK_TYPE_3 = 1
        WORK_TYPE_4 = 0

    if WORK_TYPE =='4':
        WORK_TYPE_0 = 0
        WORK_TYPE_1 = 0
        WORK_TYPE_2 = 0
        WORK_TYPE_3 = 0
        WORK_TYPE_4 = 1

    if RESIDENCE_TYPE =='1':
        RESIDENCE_TYPE_T = 1
        RESIDENCE_TYPE_F = 0
    else:
        RESIDENCE_TYPE_T = 0
        RESIDENCE_TYPE_F = 1

    if SMOKING_STATUS =='1':
        SMOKING_STATUS_T = 1
        SMOKING_STATUS_F = 0
    else:
        SMOKING_STATUS_T = 0
        SMOKING_STATUS_F = 1

    test_set = np.array([SEX_T, SEX_F, AGE, HYPERTENSION_T, HYPERTENSION_F, HEART_DISEASE_T, HEART_DISEASE_F,
                         WORK_TYPE_0, WORK_TYPE_1, WORK_TYPE_2, WORK_TYPE_3, WORK_TYPE_4, RESIDENCE_TYPE_T, RESIDENCE_TYPE_F,
                         AVG_GLUCOSE_LEVEL, BMI, SMOKING_STATUS_T, SMOKING_STATUS_F]).reshape(1, 18)
    test_set_scaled = scaler.transform(test_set)
    print(test_set_scaled.shape)
    print(test_set_scaled)
    rate = kerasmodel.predict(test_set_scaled)
    return render_template('stroke/result.html', rate=rate,
                           SEX=SEX, AGE=AGE, HYPERTENSION=HYPERTENSION, HEART_DISEASE=HEART_DISEASE, WORK_TYPE=WORK_TYPE,
                           RESIDENCE_TYPE=RESIDENCE_TYPE, AVG_GLUCOSE_LEVEL=AVG_GLUCOSE_LEVEL, BMI=BMI,
                           SMOKING_STATUS=SMOKING_STATUS)

@app.route('/hypertension_result', methods=['POST'])
def hypertension_result():
    model = load_model('c:/Health Analysis/HA_total/hypertension_model.h5')
    age = int(request.form['age'])
    trestbps = int(request.form['trestbps'])
    thalach = int(request.form['thalach'])
    oldpeak = float(request.form['oldpeak'])
    sex = request.form['sex']
    if sex == "male":
        male = 1
        female = 0
        gender = '남성'
    else:
        male = 0
        female = 1
        gender = '여성'
    cp = request.form['cp']
    if cp == "N":
        cp_n = 1
        cp_y = 0
    else:
        cp_n = 0
        cp_y = 1
    fbs = float(request.form['fbs'])
    if fbs <= 120:
        fbs_n = 1
        fbs_y = 0
    else:
        fbs_n = 0
        fbs_y = 1
    ecg = request.form['ecg']
    if ecg == "N":
        ecg_n = 1
        ecg_y = 0
    else:
        ecg_n = 0
        ecg_y = 1
    exang = request.form['exang']
    if exang == "N":
        exang_n = 1
        exang_y = 0
    else:
        exang_n = 0
        exang_y = 1
    slope = request.form['slope']
    if slope == "N":
        slope_n = 1
        slope_y = 0
    else:
        slope_n = 0
        slope_y = 1
    ca = request.form['ca']
    if ca == "N":
        ca_n = 1
        ca_y = 0
    else:
        ca_n = 0
        ca_y = 1
    test_set = [[age, trestbps, thalach, oldpeak, female, male, cp_n, cp_y,
                 fbs_n, fbs_y, ecg_n, ecg_y, exang_n, exang_y, slope_n, slope_y,
                 ca_n, ca_y]]
    scaler = joblib.load("c:/Health Analysis/HA_total/scaler.sav")
    test_set = scaler.transform(test_set)
    rate = model.predict(test_set)
    if rate >= 0.5:
        result = 'hypertension'
    else:
        result = 'non_hypertension'
    return render_template('hypertension/result.html',
                           rate='{:.2f}%'.format(rate[0][0]*100), result=result,
                           age=age, trestbps=trestbps, thalach=thalach, oldpeak=oldpeak,
                           sex=gender, cp=cp, fbs=fbs, ecg=ecg, exang=exang, slope=slope, ca=ca)

@app.route('/diabetes_result', methods=['POST'])
def diabetes_result():
    model = load_model('C:/Health Analysis/HA_total/neo_keras.h5')
    scaler = joblib.load('C:/Health Analysis/HA_total/scaler.model')

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
                           HAC=HAC, GH=GH, MH=MH, PH=PH, DW=DW, stroke=stroke, HBP=HBP)

if __name__ == '__main__':
    app.run(port=8888, threaded=False)
