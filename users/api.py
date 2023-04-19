from flask_restful import Resource, reqparse
from bson import ObjectId
from models import UserSchema
from users import users_collection, api
from flask import jsonify
from marshmallow import ValidationError

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('email', type=str, required=True)
parser.add_argument('password', type=str, required=True)


class UserListResource(Resource):
    def get(self):
        users = users_collection.find()
        return jsonify({'users': [user for user in users]})

    def post(self):
        args = parser.parse_args()
        try:
            user = UserSchema().load(args)
            user['id'] = str(ObjectId())
            users_collection.insert_one(user)
            return jsonify(user)
        except ValidationError as err:
            return jsonify(err.messages), 400


class UserResource(Resource):
    def get(self, user_id):
        user = users_collection.find_one({'id': user_id})
        if user:
            return jsonify(user)
        else:
            return jsonify({'message': 'User not found'}), 404

    def put(self, user_id):
        args = parser.parse_args()
        try:
            UserSchema().load(args)
            users_collection.update_one({'id': user_id}, {'$set': args})
            user = users_collection.find_one({'id': user_id})
            return jsonify(user)
        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, user_id):
        result = users_collection.delete_one({'id': user_id})
        if result.deleted_count > 0:
            return jsonify({'message': 'User deleted'})
        else:
            return jsonify({'message': 'User not found'}), 404


api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<string:user_id>')
