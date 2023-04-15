from users import app, db
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, flash, request
from users.models import User


# Home Route
@app.route("/", methods=['GET'])
def home():
    resp = jsonify("Welcome to student API")
    return resp


# Add user Route
@app.route("/users", methods=['POST'])
def add_user():
    _json = request.json
    User_add = User(name=_json['name'], email=_json['email'], password=_json['password'])

    # validate the recieved values
    if User_add.name and User_add.email and User_add.password and request.method == 'POST':


        # save details
        id = db.db.user.insert_one({'name': User_add.name, 'email': User_add.email, 'password': User_add.password})
        resp = jsonify("User is added Successfully")
        resp.status_code = 200
        return resp

    else:
        return not_found()


@app.route('/users')
def users():
    users = db.db.user.find()
    resp = dumps(users)
    return resp



@app.route('/users/<id>')
def user(id):
    user = db.db.user.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp

@app.route("/users/<id>", methods=['PUT'])
def update_user(id):
    _json = request.json
    User_add = User(name=_json['name'], email=_json['email'], password=_json['password'])

    # validate the recieved values
    if User_add.name and User_add.email and User_add.password and request.method == 'PUT':


        # save details
        db.db.user.update_one({'_id': ObjectId(id['$oid']) if '$oid' in id else ObjectId(id)},
                                 {'$set': {'name': User_add.name, 'email': User_add.email, 'pwd': User_add.password}})
        resp = jsonify("User is updated Successfully")
        resp.status_code = 200
        return resp

    else:
        return not_found()

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
	db.db.user.delete_one({'_id': ObjectId(id)})
	resp = jsonify('User deleted successfully!')
	resp.status_code = 200
	return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
