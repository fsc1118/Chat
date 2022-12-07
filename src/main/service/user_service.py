'''
    create user with username and password
    :param username: username
    :param password: password
    :return: 1 if success, 2 if username already exist
'''
from .encrypt import encrypt, compare_passwords
from .auth import generate_token, generate_expiration_timestamp
import sys
sys.path.append("..")
from dao.user import UserDAO

'''
    create user with username and password
    :param username: username
    :param password: password
    :return: auth_token if success, "" if username already exist
'''
def create_user_service(username:str, password:str)->str:
    # Check if the username already exists
    if UserDAO.if_username_exist(username):
        return ""
    # Create the user
    token = generate_token()
    UserDAO.create_user(username, encrypt(password), token, generate_expiration_timestamp())
    return token

'''
    login with username and password
    :param username: username
    :param password: password
    :return: auth_token if success, "" if password is incorrect or username does not exist
'''
def login_service(username:str, password:str)->str:
    # Check if the username exists
    if not UserDAO.if_username_exist(username):
        return ""
    # Check if the password is correct
    encrpyed_password = UserDAO.get_password_by_username(username, password)
    if compare_passwords(password, encrpyed_password):
        return UserDAO.get_token_by_username(username)
    else:
        return ""
    