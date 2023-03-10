from app.db import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    text = db.Column(db.String(200)) 
    createdAt = db.Column(db.DateTime(timezone=False))
    doneAt = db.Column(db.DateTime(timezone=False))
    deletedAt = db.Column(db.DateTime(timezone=False))
