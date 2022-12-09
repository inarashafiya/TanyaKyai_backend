from app import db
from app.model.tanya import Tanya
from app.model.gambar import Gambar

class Post(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    isi = db.Column(db.String(25000), nullable=False)
    tanya_id = db.Column(db.BigInteger, db.ForeignKey('tanya.id'), nullable=True)
    komentar = db.relationship('Komentar', backref='post', lazy=True)
    # gambar_id = db.relationship('Gambar', backref='post', nullable=True)   
    def __repr__(self):
        return '<Post {}>'.format(self.name)