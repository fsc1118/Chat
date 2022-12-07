from .util import Util
class PostDAO:
    __TABLE_NAME = "Post"
    @staticmethod
    def create_post(username:str, title:str, content:str)->None:
        conn = Util.get_connection()
        cursor = conn.cursor()
        # Insert the post into the database
        cursor.execute("INSERT INTO " + PostDAO.__TABLE_NAME + " (username, title, content) VALUES (?, ?, ?)", username, title, content)
        conn.commit()
        Util.close_connection(conn)