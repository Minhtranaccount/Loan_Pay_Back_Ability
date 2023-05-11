# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
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
    return render_template("form.html")

# Query the database 
@app.route("/send", methods=["GET", "POST"])
def send():
    print("Hello")
    if request.method == "POST":
        labels = ["CLIENT WILL PAY BACK ALL THE LOAN", "CLIENT WON'T PAY BACK ALL THE LOAN"]

        purpose_list = [0,0,0,0,0,0,0]

        if request.form["Purpose of the Loan"] == "all_other":
            purpose_list = [1,0,0,0,0,0,0]
        if request.form["Purpose of the Loan"] == "credit_card":
            purpose_list = [0,1,0,0,0,0,0]
        elif request.form["Purpose of the Loan"] == "debt_consolidation":
            purpose_list = [0,0,1,0,0,0,0]
        elif request.form["Purpose of the Loan"] == "educational":
            purpose_list = [0,0,0,1,0,0,0]
        elif request.form["Purpose of the Loan"] == "home_improvement":
            purpose_list = [0,0,0,0,1,0,0]
        elif request.form["Purpose of the Loan"] == "major_purchase":
            purpose_list = [0,0,0,0,0,1,0]
        else:
            purpose_list = [0,0,0,0,0,0,1]
   
        index = model.predict(
        [
            [
            float(request.form["Credit Policy"]),
            float(request.form["Interest Rate"]),
            float(request.form["Installments"]),
            float(request.form["Annual Income of Borrower"]),
            float(request.form["Debt to Income Ratio"]),
            float(request.form["Credit Score of Borrower"]),
            float(request.form["Days with Credit line"]),
            float(request.form["revol balance"]),
            float(request.form["Revol util"]),
            float(request.form["Inquiries for last 6 months"]),
            float(request.form["Dealing 2 years"]),
            float(request.form["Public records"]),
            purpose_list[0],
            purpose_list[1],
            purpose_list[2],
            purpose_list[3],
            purpose_list[4],
            purpose_list[5],
            purpose_list[6],       
            ],
        ]
    )[0]
        print(index)
        return render_template("outcome.html", Outcome = labels[index] )

    else:
        return render_template("form.html")


if __name__ == "__main__":

    # run the flask app
    app.run()
