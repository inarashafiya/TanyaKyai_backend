from app import db
import json
from app.model.gambar import Gambar

class Komentar(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    isi = db.Column(db.String(1000), nullable=False)
    post_id = db.Column(db.BigInteger, db.ForeignKey('post.id'))
    name = db.Column(db.String(1000), nullable=False)
    picture = db.Column(db.String(1000), nullable=False)
    
    def __repr__(self):
        return '<Komentar {}>'.format(self.name)