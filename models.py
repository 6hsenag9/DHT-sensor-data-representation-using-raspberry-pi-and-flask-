from lab_app import db

class Readings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.Float, index=True)
    hum = db.Column(db.Integer, index=True)
    datetime = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return f'<temp:{self.temp} hum:{self.hum},date:{self.datetime}'


