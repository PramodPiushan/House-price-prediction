from flask import Flask, request, jsonify
import utill

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'location': utill.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_Home_price', methods=['GET', 'POST'])
def predict_Home_price():
    Baths = float(request.form['Lengh_of_rows'])
    Beds = request.form['number_of_rows']
    Land_size = float(request.form['temperature'])
    House_size = int(request.form['soil_condition'])
    location = request.form['crop']

    response = jsonify({
        'expected_yeild': utill.predict_Home_price(Baths,Beds,Land_size,House_size,location)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
