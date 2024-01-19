from flask import Flask, render_template
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
#CORS(app)



@app.route("/home")
def index():
    return render_template('index.html')

@app.route("/oil-changes")
def oilChanges():
    return render_template('oil-changes.html')

@app.route("/state-inspections")
def stateInspections():
    return render_template('state-inspections.html')

@app.route("/brakes")
def brakes():
    return render_template('brakes.html')

@app.route("/ac-diagnosis")
def ac_diagnosis():
    return render_template('ac-diagnosis.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
