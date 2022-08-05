from flask import Flask, render_template
from flask import session, request, jsonify, flash
from markupsafe import escape
from flask import redirect, url_for
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = "somesecrettextusedtoencryptsessiondatapleasedon'tshareittoanyone"

def get_db():
    db = sql.connect("weather.db")
    cursor = db.cursor()
    return db, cursor

def close_db(db, cursor):
    cursor.close()
    db.close()

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
    username = escape(request.form["username"]).lower().strip()
    password = escape(request.form["password"])
    return f"you are trying to login with {username} {password}"

@app.route("/mk_signup", methods=["POST"])
def mk_signup():
    first_name = escape(request.form["fname"]).lower().strip()
    last_name = escape(request.form["lname"]).lower().strip()
    email = escape(request.form["email"]).lower().strip()
    username = escape(request.form["uname"]).lower().strip()
    password = escape(request.form["password"]).lower().strip()
    # email unique, username unique
    db, cursor = get_db()
    cursor.execute("SELECT * FROM user WHERE username=? OR email=?", (username, email))
    # ("sachin", "sachin@gmail.com", "sachin", "yadav", "yahoo")
    if cursor.fetchone():
        # account already exists
        flash("Username or Email already registred with Us!")
        flash("Choose Different Username or Email to create new account!")
        
    else:
        # account does not exists
        cursor.execute(
            "INSERT INTO user VALUES (?, ?, ?, ?, ?)", 
            (username, email, first_name, last_name, password))
        db.commit()
        close_db(db, cursor)
        flash("Your account has successfully created! Please Login to Continue")
    
    return redirect(url_for("index"))
        



# @app.route("/query/<string:name>")
# def query(name):
#     s = ""
#     for i in range(1, 11):
#         s += name*i + "<br>"
#     return s


@app.route("/show_all")
def show_all():
    db, cursor = get_db()
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    close_db(db, cursor)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
    #host=localhost, port=5000
