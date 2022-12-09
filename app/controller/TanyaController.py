from app.model.tanya import Tanya 
from sqlalchemy import and_
from app import response, app, db
from flask import request

def TanyaList():
    try:
        tanya = Tanya.query.all()
        data = transform(tanya)
        return response.success(data, "Data berhasil didapatkan")
    except Exception as e:
        print(e)
        
def singleTransform(tanya):
    data = {
        'id' : tanya.id,
        'isi' : tanya.isi,
        # 'googleuid' : tanya.googleuid,
    }
    return data

def transform(tanya):
    array = []
    for i in tanya:
        if i.answered == False:
            array.append(singleTransform(i))
    return array

def TanyabyID(id):
    try:
        tanya = Tanya.query.filter(id=id).first()
        data = singleTransform(tanya)
        return response.success(data, "Data berhasil didapatkan")
    
    except Exception as e:
        print(e)

    # id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    # googleuid = db.Column(db.String(100), nullable=False)
    # isi = db.Column(db.String(1500), nullable=False)       
     
        
def TanyaAdd():
    try:
        output = request.get_json()
        isi = output['isi']
        # if not output['googleuid']:
        #     googleuid = 1
        # else:
        #     googleuid = output['googleuid']
        tanyaAdd = Tanya(isi=isi )
        db.session.add(tanyaAdd)
        db.session.commit()

        return response.success(output, 'berhasil tambah pertanyaan')
    except Exception as e:
        print(e)
        
def TanyaDelete(id):
    try:
        tanya = Tanya.query.filter_by(id=id).first()
        if not tanya:
            return response.badRequest([], 'Data Dosen Kosong...')
        
        db.session.delete(tanya)
        db.session.commit()

        return response.success('', 'Berhasil menghapus data!')
    except Exception as e:
        print(e)