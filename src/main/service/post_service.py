def create_new_post(username:str, title:str, content:str):
    # Create a new post
    PostDAO.create_post(username, title, content)
    return "Post created", 200