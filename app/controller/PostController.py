from app.model.post import Post
from app.model.tanya import Tanya 
from app.model.komentar import Komentar
from app import response, app, db
from flask import request, jsonify, make_response, Response


def PostList():
    try:
        post = Post.query.all()
        data = transform(post)
        return response.success(data, "Data berhasil didapatkan")
    except Exception as e:
        print(e)
                
def transform(datas):
    array = []
    
    for i in datas:
        array.append(singleTransform(i))
    return array

def singleTransform(data):
    if data.tanya_id is not None:
        tanya = Tanya.query.filter_by(id=data.tanya_id).first()
        tanya = tanya.isi
        data = {
            'id' : data.id,
            'isi' : data.isi,
            'tanya_id' : data.tanya_id,
            'tanya' : tanya,
        }
    else:
        data = {
            'id' : data.id,
            'isi' : data.isi,
        }
    return data


def PostbyID(id):
    try:
        posts = Post.query.filter_by(id=id).first()
        data = singleTransform(posts)
        return response.success(data, "Data berhasil didapatkan")
    
    except Exception as e:
        print(e)

# def _build_cors_preflight_response():
#     response = Response()
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add("Access-Control-Allow-Headers", "*")
#     response.headers.add("Access-Control-Allow-Methods", "*")
#     return response

def PostAdd():
    try:
        output = request.get_json()
        # print(output)
        # output.headers.add("Access-Control-Allow-Origin", "*")
        isi = output['isi']
        if output['tanya'] is not None:
            tanya = output['tanya']
            tanya = Tanya.query.filter_by(isi=tanya).first()
            tanya_id = tanya.id
            postAdd = Post(isi = isi, tanya_id = tanya_id)
            tanya.answered = True
        else:
            postAdd = Post(isi = isi, tanya_id = None)
        
        db.session.add(postAdd)
        db.session.commit()

        return response.success(output, 'ini output')
    except Exception as e:
        print(e)
        
def PostDelete(id):
    try:
        post = Post.query.filter_by(id=id).first()
        if not post:
            return response.badRequest([], 'Data Kosong...')
        komentar = Komentar.query.filter_by(post_id=id).all()
        for i in komentar:
            db.session.delete(i)
        # db.session.delete(komentar)
        db.session.delete(post)
        db.session.commit()

        return response.success('', 'Berhasil menghapus data!')
    except Exception as e:
        print(e)
    
