from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=8000)
