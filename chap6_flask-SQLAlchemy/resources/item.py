import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required

from user import UserRegister
from security import authenticate, identity
from models.item import ItemModel

class Item(Resource):
	parser = reqparse.RequestParser()
        parser.add_argument('price',
                        type=float,
                        required=True,
                        help= "Cannot be left blank !"
                )
        parser.add_argument('store_id',
                        type=float,
                        required=True,
                        help= "Every item need a store id!"
                )         
	@jwt_required()
	def get(self,name):
		item = ItemModel.find_by_name(name)
		if item:
			return item.json()
		return {'message':'item not found'},404


	def post(self,name):
		if ItemModel.find_by_name(name):
			{'message':"An item '{}' already exists".format(name)},400

		data = Item.parser.parse_args()

		item = ItemModel(name,**data)
		
		try:
			
			item.save_to_db()
			
		except AttributeError as error:
			
			return{'message':'An error occured on inserting the ItemModel.{}'.format(error)},500
			
		return item.json(),201

	def delete(self,name):
		item = ItemModel.find_by_name(name)
		if item:
			item.delete_from_db()
		

	def put(self,name):
		data = Item.parser.parse_args()
		
		item = ItemModel.find_by_name(name)
		
		if item is None:
			item = ItemModel(name,**data)
		else:
			item.price = data['price']
		item.save_to_db()
		return item.json()


class ItemList(Resource):
	def get(self):
		return {'items': [item.json() for item in ItemModel.query.all()]}

