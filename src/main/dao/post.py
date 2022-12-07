from .util import Util
class PostDAO:
    __TABLE_NAME = "Post"
    @staticmethod
    def create_post(username:str, title:str, content:str, id:str, created_time:str, upvote: int)->None:
        conn = Util.get_connection()
        cursor = conn.cursor()
        # Insert the post into the database
        cursor.execute("INSERT INTO " + PostDAO.__TABLE_NAME + " (username, title, content, id, created_time, upvote) VALUES (?, ?, ?, ?, ?, ?)", username, title, content, id, created_time, upvote)
        conn.commit()
        Util.close_connection(conn)
    @staticmethod
    def get_posts_with_pagination(page:int)->list:
        # Convert page to offset
    # If page is 1, then return the newest 10 posts
    # If page is 2, then return the 10 posts before the newest 10 posts, and so on so forth
        conn = Util.get_connection()
        cursor = conn.cursor()
        # Microsoft Access does not support OFFSET and FETCH NEXT, so we have to use the following query
        cursor.execute("SELECT * FROM (SELECT TOP 10 * FROM (SELECT TOP " + str(page * 10) + " * FROM " + PostDAO.__TABLE_NAME + " ORDER BY created_time DESC) ORDER BY created_time ASC) ORDER BY created_time DESC")
        res = cursor.fetchall()
        Util.close_connection(conn)
        return res