import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    # to detect and accept only price value
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This cannot be blank")
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="every item needs a store id")

    @jwt_required()  # required auth for get
    def get(self, name):
        # get inserted item  in the list/database
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {"message": "item not found"}, 404

    # insert name and price

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "an item with name {} already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'],data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201  # 201 created

    # delete item
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query, (name,))

        # connection.commit()
        # connection.close()
        return {'message': 'item deleted'}

    # update or create item
    def put(self, name):  # update item
        # to just read and update the price and don't change the name
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']

            item.save_to_db()
        return item.json()


class ItemList(Resource):
    # read all items
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
