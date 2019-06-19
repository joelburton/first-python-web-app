from flask import Flask, render_template, request, jsonify
from random import randint

app = Flask(__name__)

posts = [
    {"title": "Flask is Neat", "body": "This is the body for Flask is Neat"},
    {"title": "Summer is Awesome", "body": "This is the body for Summer is Awesome"},
]

def get_lucky_num():
    return randint(1, 100)

# This the first version we wrote, where we didn't yet use templates & just
# return the HTML directly that we want

# @app.route("/")
# def homepage():
#     num = get_lucky_num()
#     return f"<b>Hi</b> {num} <i>there</i>"

@app.route("/")
def templated_homepage():
    num = get_lucky_num()

    return render_template("homepage.html", lucky_num=num, posts=posts)

@app.route("/new_post", methods=["POST"])
def add_new_post():
    title = request.form['title']
    body = request.form['body']
    # just so we can see what's happening, we'll print this to the terminal; this
    # doesn't change how the app works
    print(title, body)
    posts.append({"title": title, "body": body})
    return "<h1>New Post Added</h1>"

# This was added after John's question "can Flask be an API server and return JSON?"
@app.route("/posts.json")
def posts:
    return jsonify(posts)

# This was our example of a second, simple route
@app.route("/alvin")
def say_hi_to_alvin():
    return "<b>Hi</b> <i>alvin</i>"