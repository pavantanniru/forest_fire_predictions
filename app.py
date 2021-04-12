from flask import Flask ,render_template,request,url_for
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route("/")


def index():
    return render_template("index.html")

@app.route("/predictions",methods=["POST","GET"])

def result():

    oxygen = float(request.form['oxy'])
    temperature = float(request.form['temp'])
    humidity = float(request.form['hum'])

    data = [[oxygen,temperature,humidity]]
    result = model.predict(data)

    return render_template("result.html",oxy=oxygen,result = result)



if __name__ == "__main__":
    app.run()
