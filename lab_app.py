from flask import Flask, render_template
import Adafruit_DHT
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__, template_folder='static')
app.config.from_object(Config)
db = SQLAlchemy(app)
from models import Readings

@app.route("/")
def lab_temp():
    hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,17)
    return render_template("current.html",title="current",temp=temp,hum=hum)

@app.route("/env_db")
def env_db():
    ls = Readings.query.all()
    return render_template("env_db.html", title="monitor", ls = ls)


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080)

