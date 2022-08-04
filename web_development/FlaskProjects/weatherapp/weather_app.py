from flask import Flask, render_template
from flask import session, request

app = Flask(__name__)
app.secret_key = "somesecrettextusedtoencryptsessiondatapleasedon'tshareittoanyone"

@app.route("/temp")
def temp():
    return render_template("index.html")

@app.route("/")
def index():
    if "username" in session:
        # it means user is already logged in
        return render_template("index.html")
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/mk_login", methods=["POST"])
def mk_login():
    username = request.form["username"]
    password = request.form["password"]
    return f"you are trying to login with {username} {password}"



# @app.route("/query/<string:name>")
# def query(name):
#     s = ""
#     for i in range(1, 11):
#         s += name*i + "<br>"
#     return s


if __name__ == "__main__":
    app.run(debug=True)
    #host=localhost, port=5000
