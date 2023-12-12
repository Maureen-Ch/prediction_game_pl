import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

model = pickle.load(open("model.sav","rb"))
@app.route('/', methods=['GET'])
def prediction_index(): 
    return render_template('index.html')


@app.route('/predict/', methods=['POST'])
def result():
    venue_code = request.form['venue_code']
    opp_code = request.form['opp_code']
    hour = request.form['hour']
    day_code = request.form['day_code']

    reg = model.predict([[venue_code,opp_code,hour,day_code]])[0]
    return render_template("prediction.html", target=reg)

if __name__ == '__main__':
    app.debug = True
    app.run(
        host='0.0.0.0',
        port=5500,
        debug=True)