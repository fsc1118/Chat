import uuid
import time
import sys
sys.path.append("..")
from dao.user import UserDAO
def generate_token() -> str:
    return str(uuid.uuid4())

def generate_expiration_timestamp() -> str:
    # timestamp of 7 days from now
    return str(int(time.time()) + 7 * 24 * 60 * 60)

def __is_token_expired(token_expiration_timestamp: str) -> bool:
    return int(token_expiration_timestamp) < int(time.time())

def is_token_valid(username: str, token: str) -> bool:
    # Check if username exists
    if not UserDAO.if_username_exist(username):
        return False
    # Check if the token is valid
    if token == UserDAO.get_token_by_username(username):
        # Check if the token is expired
        if not __is_token_expired(UserDAO.get_expiration_date_by_username(username)):
            return True
        # Update the token
        UserDAO.update_token_by_username(username, generate_token(), generate_expiration_timestamp())
    return False