from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    # find the user inserted
    user = UserModel.find_by_username(username)
    # if the user and password matches return the user
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')): # to be sutiable for all versions and sys
        return user


def identity(payload):
    # return the id
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
