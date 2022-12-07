import uuid
import time
import sys
sys.path.append("..")
from dao.post import PostDAO
def create_new_post(username:str, title:str, content:str)->None:
    # Create a new post
    PostDAO.create_post(
        username=username,
        title=title,
        content=content,
        id=str(uuid.uuid4()),
        created_time=str(int(time.time())),
        upvote=0
    )

def get_posts_with_pagination(page:int)->list:
    query_result = PostDAO.get_posts_with_pagination(page=page)
    # Sanitize the query result
    res = []
    for row in query_result:
        res.append({
            "username": row.username,
            "title": row.title,
            "content": row.content,
            "id": row.ID,
            "created_time": row.created_time,
            "upvote": row.upvote
        })
    return res