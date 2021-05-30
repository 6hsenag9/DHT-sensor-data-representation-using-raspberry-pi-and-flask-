from lab_app import db
from models import Readings
import Adafruit_DHT
import datetime

def log(temp, hum, date):
    a = Readings(temp=temp, hum=hum, datetime=date)
    db.session.add(a)
    db.session.commit()

d = datetime.datetime.now()
x = d - datetime.timedelta(microseconds=d.microsecond)

hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)

if temp and hum:
    log(temp,  hum, x)
else:
    log(-999, -999, x)

