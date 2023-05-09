# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request
)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Model Setup
#################################################

from joblib import load
model_path = "model.joblib"
print("Loading model...")
model = load(model_path)

#################################################
# Web User Interface - Front End
#################################################
# note that UI routes return a html response
# you can add as many html pages as you need
# below is an example to get you started...

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

#################################################
# API - Back End
#################################################


@app.route("/score", methods=["POST"])
def predict():
    labels = ["0", "1"]
    index = model.predict(
        [
            [
            float(request.form["Credit Policy"]),
            float(request.form["Interest Rate"]),
            float(request.form["Loan Installments"]),
            float(request.form["Annual Income of Borrower"]),
            float(request.form["Debt to income Ratio"]),
            float(request.form["Credit Score"]),
            float(request.form["Days with Credit line"]),
            float(request.form["revol balance"]),
            float(request.form["Revol util"]),
            float(request.form["Inquiries for last 6 months"]),
            float(request.form["Dealing 2 years"]),
            float(request.form["Public records"]),
            float(request.form["Purpose of the Loan"]),           
            ],
        ]
    )[0]
    return jsonify(f"Predicted Loan status: {labels[index]}")


if __name__ == "__main__":

    # run the flask app
    app.run()
