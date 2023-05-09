# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect
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

# Query the database 
@app.route("/LoanRequestForm", methods=["GET", "POST"])
def send():
    if request.method == "POST":
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
            #float(request.form["Purpose of the Loan"]),           
            ],
        ]
    )[0]
        print(index)
        return render_template("Outcome.html", Outcome = labels[index] )
    else:
        return render_template("form.html")


if __name__ == "__main__":

    # run the flask app
    app.run()
