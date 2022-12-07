from flask import Flask, request
from service.user_service import create_user_service, login_service
from service.auth import is_token_valid
from service.post_service import create_new_post
app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    # Get the username, password, and auth token from the request body
    username = request.json["username"]
    password = request.json["password"]
    if not username:
        return "Username is missing", 400
    if not password:
        return "Password is missing", 400
    res = login_service(username, password)
    if res != "":
        body = {
            "username": username,
            "token": res
        }
        return body, 200
    else:
        return "Incorrect username or password", 400

@app.route("/register", methods=["POST"])
def register():
    # Get the username and password from the request body
    username = request.json["username"] 
    password = request.json["password"]
    # Check if username is present in request body
    if not username:
        return "Username is missing", 400
    # Check if password is present in request body
    if not password:
        return "Password is missing", 400
    res = create_user_service(username, password)
    if res != "":
        body = {
            "username": username,
            "token": res
        }
        return body, 200
    elif res == "":
        return "Username already exists", 400
    else:
        return "Error", 500

@app.route("/post", methods=["POST"]):
def post():
    # Get username and token from request body
    username = request.json["username"]
    token = request.json["token"]
    # Check if username is present in request body
    if not username:
        return "Username is missing", 400
    # Check if token is present in request body. If not, return Unauthorized
    if not token:
        return "Token is missing", 401
    # Check if the token is valid. If not, return Unauthorized
    if not is_token_valid(username, token):
        return "Unauthorized", 401
    # Get the post from the request body
    title = request.json["title"]
    content = request.json["content"]
    create_new_post(username, title, content)
    return "Post created", 200