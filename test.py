from lab_app import db
from models import Readings

ls = Readings.query.all()
for i in ls:
    l = []
    t = i.temp
    d = i.datetime
    l.append(t)
    l.append(d)
    print(l)

