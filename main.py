import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

main = Flask(__name__, template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

@main.route('/predict_api',methods=['POST'])

if __name__ == "__main__":
    app.run(debug=True)
