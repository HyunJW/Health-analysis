from flask import Flask,render_template,request
from keras.models import load_model
import numpy as np
import joblib
app = Flask(__name__)
@app.route('/',methods=['GET'])
def main():
    return render_template('miniproject/input.html')

@app.route('/result',methods=['POST'])
def result():
    model = load_model('c:/data/minitot/miniproject1.h5')
    scaler = joblib.load('c:/data/minitot/miniscaler.sav')
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

    test_set = np.array([SEX_T, SEX_F, AGE, HYPERTENSION_T, HYPERTENSION_F, HEART_DISEASE_T,HEART_DISEASE_F,
                         WORK_TYPE_0,WORK_TYPE_1,WORK_TYPE_2,WORK_TYPE_3,WORK_TYPE_4,RESIDENCE_TYPE_T,RESIDENCE_TYPE_F,
                         AVG_GLUCOSE_LEVEL,BMI,SMOKING_STATUS_T,SMOKING_STATUS_F]).reshape(1,18)
    test_set_scaled=scaler.transform(test_set)
    rate= model.predict(test_set_scaled)
    return render_template('miniproject/result.html',rate=rate,
                           SEX=SEX, AGE=AGE,HYPERTENSION=HYPERTENSION, HEART_DISEASE=HEART_DISEASE,WORK_TYPE=WORK_TYPE,
                           RESIDENCE_TYPE=RESIDENCE_TYPE, AVG_GLUCOSE_LEVEL=AVG_GLUCOSE_LEVEL, BMI=BMI,
                           SMOKING_STATUS=SMOKING_STATUS)
if __name__ == '__main__':
    #웹브라우저에서 실행할 때 http://localhost로 하면 느림
    #http://127.0.0.1로 할 것
    app.run(port=8000, threaded=False)