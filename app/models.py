from . import db

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(500))
    severity = db.Column(db.String(20))
    reporter = db.Column(db.String(50))
