from app import db

class Document(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)

    def __repr__(self):
        return '<Document {}>'.format(self.n)