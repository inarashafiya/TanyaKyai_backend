from app.model.fatwa import Fatwa
from app.model.document import Document

from app import response, app, db
from flask import request

class Fatwa(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    isi = db.Column(db.String(255), nullable=False)
    docs_id = db.Column(db.BigInteger, db.ForeignKey('document.id'), nullable=True)

def FatwaList():
    try:
        fatwas = Fatwa.query.all()
        data = transform(fatwas)
        return response.success(data, "Data berhasil didapatkan")
    except Exception as e:
        print(e)

def singleTransform(fatwa):
    data = {
        'id' : fatwa.id,
        'isi' : fatwa.isi,
        'docs_id' : fatwa.docs_id
    }
    return data

def transform(fatwas):
    array = []
    for i in fatwas:
        array.append(singleTransform(i))
    return array