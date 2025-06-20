from flask import Flask, request, jsonify, render_template
from server import util
app = Flask(__name__)

util.load_saved_artifacts()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sqft = float(request.form['sqft'])
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        location = request.form['location']
        estimated_price = util.get_estimated_price(location, sqft, bhk, bath)
        return render_template('index.html',
                               locations=util.get_location_names(),
                               prediction_text=f"Estimated Price : ₹{estimated_price:,.2f} Lakh")
    else:
        return render_template('index.html', locations=util.get_location_names())




@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# @app.route('/predict', methods = ['POST'])
# def predict_price():
#     sqft = float(request.form['sqft'])
#     bhk = int(request.form['bhk'])
#     bath = int(request.form['bath'])
#     location = request.form['location']

#     estimated_price = util.get_estimated_price(location, sqft, bhk, bath)

#     return render_template('index.html',  prediction_text = f"Estimated Price : Rs. {estimated_price:,.2f} Lakh.")

if __name__ == '__main__' : 
    app.run(debug = True)