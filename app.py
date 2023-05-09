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
model_path = os.environ.get('MODEL_PATH', '') or "model.joblib"
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

# TODO: Add more routes if needed

#################################################
# API - Back End
#################################################
# we will use '/api/..' for our api within flask application
# note that api returns a JSON response

// Get the url endpoint
const _url = "";

// Initialize a data variable to hold JSON data here so that it can be used by various functions
let data;

// Fetch the JSON loan data using then function
d3.json(_url).then(function(data_response) {
    
    // Let the data variable hold the JSON data
    data = data_response;

    // Append options for the dropdown menu
    appendOptions();

    // Call the optionChanged function when the user selects a new option from the dropdown menu (the trigger event)
    d3.select("#selPurpose of the Loan").on("change", function() {
        optionChanged(this.value);
    });

    // Initialise the dashboard
    init();

});

# below is an example to get you started...

@app.route("/score", methods=["POST"])
def predict():
    labels = [0, 1]
    index = model.predict(
        [
            [
            float(request.form["Purpose of the Loan"]),
            float(request.form["Loan Installments"]),
            float(request.form["Annual Income of Borrower"]),
            float(request.form["Credit Score"]),
            float(request.form["Debt to income Ratio"]),
            float(request.form["Days with Credit line"]),
            float(request.form["revol balance"]),
            float(request.form["Revol util"]),
            float(request.form["Inquiries for last 6 months"]),
            float(request.form["Dealing 2 years"]),
            float(request.form["Public records"]),            
            ],
        ]
    )[0]
    return jsonify(f"Predicted Loan status: {labels[index]}")


if __name__ == "__main__":

    # run the flask app
    app.run()
