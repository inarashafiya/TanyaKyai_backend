from app import app, response
from app.controller import UserController
from app.controller import TanyaController
from app.controller import PostController
from app.controller import KomenController
from flask import request, Response, jsonify
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
from flask_cors import cross_origin

@app.route('/')
@cross_origin()
def home():
    resp = Response("hello") #here you could use make_response(render_template(...)) too
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['ngrok-skip-browser-warning'] = "69420"
    return resp
# def index():
#     return Response(headers={'Access-Control-Allow-Origin':'*'})

#create post app route
@app.route('/posts', methods=['GET', 'POST'])
@cross_origin()
def Posts():
    if request.method == 'GET':
        return PostController.PostList()
    elif request.method == 'POST':
        return PostController.PostAdd()
    else:
        return response.badRequest([], 'Invalid Method')
    
@app.route('/posts/<id>', methods=['GET', 'DELETE'])
@cross_origin()
def PostbyID(id):
    if request.method == 'GET':
        return PostController.PostbyID(id)
    else:
        return PostController.PostDelete(id)


@app.route('/questions', methods=['GET', 'POST'])
@cross_origin()
def Tanyas():
    if request.method == 'GET':
        return TanyaController.TanyaList()
    elif request.method == 'POST':
        return TanyaController.TanyaAdd()


@app.after_request
def add_header(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response


@app.route('/questions/<id>', methods=['GET', 'DELETE'])
@cross_origin()
def TanyabyID(id):
    if request.method == 'GET':
        return TanyaController.TanyabyID(id)
    else:
        return TanyaController.TanyaDelete(id)
    

@app.route('/file-upload', methods=['POST'])
@cross_origin()
def uploads():
    return UserController.upload()

@app.route('/comments_post/<id>', methods=['GET'])
@cross_origin()
def Comment(id):
    return KomenController.KomenList(id)

@app.route('/comments_post', methods=['POST'])
@cross_origin()
def addComment():
    return KomenController.KomenAdd()

@app.route('/comments/<id>', methods=['DELETE'])
@cross_origin()
def DeleteComments(id):
    return KomenController.KomenDelete(id)


# @app.route('/bio', methods=['POST'])
# def bio():
#     return UserController.bio()

# @app.route('/image-upload', methods=['POST'])
# @cross_origin()
# def parse_markdown():
#     image = request.files['image']
    
#     return UserController.image_upload()