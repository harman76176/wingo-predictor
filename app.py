from flask import Flask, render_template
import pickle
from scraper import get_latest_results
import numpy as np

app = Flask(__name__)

model = pickle.load(open("wingo_model.pkl", "rb"))

@app.route("/")
def home():
    last = get_latest_results()
    x_input = np.array(last).reshape(1, -1)
    predicted = model.predict(x_input)[0]
    return render_template("index.html", last=last, prediction=predicted)

if __name__ == "__main__":
    app.run(debug=True)
