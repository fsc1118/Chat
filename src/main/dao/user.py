from .util import Util
class UserDAO:
    __TABLE_NAME = "User"
    @staticmethod
    def create_user(username:str, password:str, token:str, expiration_date:str)->None:
        # Encrypt the password
        conn = Util.get_connection()
        cursor = conn.cursor()
        # Insert the user into the database
        cursor.execute("INSERT INTO " + UserDAO.__TABLE_NAME + " (username, password, token, expiration_date) VALUES (?, ?, ?, ?)", username, password, token, expiration_date)
        conn.commit()
        Util.close_connection(conn)
    @staticmethod
    def get_password_by_username(username:str, password:str)->str:
        conn = Util.get_connection()
        cursor = conn.cursor()
        # Check if the user exists in the database
        cursor.execute("SELECT * FROM " + UserDAO.__TABLE_NAME + " WHERE username = ?", username)
        row = cursor.fetchone()
        Util.close_connection(conn)
        if row:
            return row.password
        raise Exception("User not found")
    
    @staticmethod
    def if_username_exist(username:str)->bool:
        conn = Util.get_connection()
        cursor = conn.cursor()
        # Check if the user exists in the database
        cursor.execute("SELECT * FROM " + UserDAO.__TABLE_NAME + " WHERE username = ?", username)
        row = cursor.fetchone()
        Util.close_connection(conn)
        if row:
            return True
        return False
    
    @staticmethod
    def get_token_by_username(username:str)->str:
        conn = Util.get_connection()
        cursor = conn.cursor()
        # Check if the user exists in the database
        cursor.execute("SELECT * FROM " + UserDAO.__TABLE_NAME + " WHERE username = ?", username)
        row = cursor.fetchone()
        Util.close_connection(conn)
        if row:
            return row.token
        raise Exception("User not found")

    @staticmethod
    def update_token_by_username(username:str, token:str, timestamp:str)->None:
        conn = Util.get_connection()
        cursor = conn.cursor()
        # Update the token
        cursor.execute("UPDATE " + UserDAO.__TABLE_NAME + " SET token = ?, expiration_date = ? WHERE username = ?", token, timestamp, username)
        conn.commit()
        Util.close_connection(conn)