from flask import Flask, render_template, request
from keras.models import load_model
from joblib import load

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('hypertension/input.html')

@app.route('/hypertension_result', methods=['POST'])
def hypertension_result():
    model = load_model('c:/data/minitot/hypertension_model.h5')
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
    scaler = load("c:/data/minitot/scaler.sav")
    test_set = scaler.transform(test_set)
    rate = model.predict(test_set)
    if rate >= 0.5:
        result = 'hypertension'
    else:
        result = 'non_hypertension'
    return render_template('hypertension/hypertension_result.html',
                           rate='{:.2f}%'.format(rate[0][0]*100), result=result,
                           age=age, trestbps=trestbps, thalach=thalach, oldpeak=oldpeak,
                           sex=gender, cp=cp, fbs=fbs, ecg=ecg, exang=exang, slope=slope, ca=ca)

if __name__ == '__main__':
    app.run(port=8000, threaded=False)
