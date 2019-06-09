import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username,password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        # # get the data by username inserted
        # query = "SELECT * FROM users WHERE username = ?"
        # result = cursor.execute(query, (username,)) # to make username run first
        # row = result.fetchone()
        # if row:
        #     user = cls(*row) # row[0] id, row[1] username, row[2] password
        # else:
        #     user = None
        #
        # connection.close()
        # return user

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        # connection = sqlite3.connect("testDatabase.db")
        # cursor = connection.cursor()
        # # get the data by id inserted
        # query = "SELECT * FROM users WHERE id = ?"
        #
        # result = cursor.execute(query, (_id,))  # to make id run first
        # row = result.fetchone()
        # if row:
        #     _id = cls(*row)
        # else:
        #     _id = None
        #
        # connection.close()
        # return _id