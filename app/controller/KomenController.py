from app.model.post import Post
from app.model.komentar import Komentar 

from app import response, app, db
from flask import request, jsonify, make_response, Response


def KomenList(id):
    try:
        post = Post.query.filter_by(id=id).first()
        komen = Komentar.query.filter_by(post_id=post.id).all()
        data = transform(komen)
        return response.success(data, "Data berhasil didapatkan")
    except Exception as e:
        print(e)
                
def transform(datas):
    array = []
    
    for i in datas:
        array.append(singleTransform(i))
    return array

def singleTransform(data):
    data = {
            'picture' : data.picture,
            'name' : data.name,
            'id' : data.id,
            'isi' : data.isi,
            'post_id' : data.post_id,
        }
    return data


def KomenAdd():
    try:
        output = request.get_json()
        # print(output)
        # output.headers.add("Access-Control-Allow-Origin", "*")
        isi = output['isi']
        name = output['name']
        picture = output['picture']
        post_id = output['post_id']
        komen_add = Komentar(isi=isi, name=name, picture=picture, post_id=post_id)
                
        db.session.add(komen_add)
        db.session.commit()

        return response.success(output, 'ini output')
    except Exception as e:
        print(e)
        
def KomenDelete(id):
    try:
        komen = Komentar.query.filter_by(id=id).first()
        if not komen:
            return response.badRequest([], 'Data Kosong...')
        
        db.session.delete(komen)
        db.session.commit()

        return response.success('', 'Berhasil menghapus data!')
    except Exception as e:
        print(e)