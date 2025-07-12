import numpy as np
from flask import Flask, request, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    try:
        n = float(request.form['n'])
        p = float(request.form['p'])
        k = float(request.form['k'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        features = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
        prediction = model.predict(features)
        return render_template("index.html", prediction_text="The Predicted Crop is {}".format(prediction[0]))
    except Exception as e:
        print("Error during prediction:", e)
        return render_template("index.html", prediction_text="An error occurred during prediction.")


if __name__ == "__main__":
    flask_app.run(debug=True)