from app import db
import json
from app.model.gambar import Gambar

class Tanya(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    # googleuid = db.Column(db.String(100), nullable=True)
    isi = db.Column(db.String(25000), nullable=False)
    answered = db.Column(db.Boolean, nullable=False, default=False)
    def __repr__(self):
        return '<Tanya {}>'.format(self.name)