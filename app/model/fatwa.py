from app import db
from app.model.gambar import Gambar

class Fatwa(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    isi = db.Column(db.String(255), nullable=False)
    docs_id = db.Column(db.BigInteger, db.ForeignKey('document.id'), nullable=True)
    
    def __repr__(self):
        return '<Fatwa {}>'.format(self.n)