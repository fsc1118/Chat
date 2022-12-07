import hashlib

'''
    This file contains the functions to encrypt the password
    :param password: The password to encrypt
    :return: The encrypted password
'''
def encrypt(password:str)->str:
    # Encrypt the password using sha256
    return hashlib.sha256(password.encode()).hexdigest()

'''
    This function compares the password with the hashed password
    :param password: The password to compare
    :param hashed_password: The hashed password to compare with
    :return: True if the passwords match, False otherwise
'''
def compare_passwords(password, hashed_password)->bool:
    # Compare the password with the hashed password
    return encrypt(password) == hashed_password