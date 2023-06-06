from flask import Flask 
import flask 
import string
import secrets

app= Flask(
    __name__,
    static_url_path="",
    template_folder="../UI/templates/",
    static_folder = "../UI/static/",
    )
app.secret_key="duw283rgdwq"

@app.route("/")
@app.route("/homepage")
def home():
    topic = "HELLO EVERYONE"
    return flask.render_template("homepage.html",header=topic)

@app.route("/login")
def login():
    length=16
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for i in range(length))
    return flask.render_template("login.html",suggested_password=password,action="/login_post")

# @app.route("/login_post", methods = ["POST"])
# def post_login():
#     name = flask.request.form["username"]
#     password = flask.request.form["password"]
#     print(name)
#     print(password)
#     return flask.redirect("/login")


@app.route("/login_post", methods = ["POST"])
def post_login():
    name = flask.request.form["username"]
    password = flask.request.form["password"]
    print(name)
    print(password)
    if len(name or password) < 9:
        return flask.render_template("Errpage.html")
    else:
        return flask.render_template("Welcomepage.html")
    














