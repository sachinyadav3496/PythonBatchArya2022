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

@app.route("/")
def index():
    if "username" in session:
        # it means user is already logged in
        username = session["username"]
        db, cursor = get_db()
        cursor.execute("SELECT * FROM user WHERE username=?", (username,))
        row = cursor.fetchone()
        first_name = row[2].title()
        last_name = row[3].title()
        return render_template("index.html", first_name=first_name, last_name=last_name)
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/mk_login", methods=["POST"])
def mk_login():
    username = escape(request.form["username"]).lower().strip()
    password = escape(request.form["password"])
    db, cursor = get_db()
    cursor.execute("SELECT * FROM user WHERE username=?", (username,))
    row = cursor.fetchone()
    if row:
        # row = ('sachin', 'sachin@gmail.com', 'sachin', 'yadav', 'redhat')
        if password == row[-1]:
            # user is loogged in
            session["username"] = username
            flash(f"!Welcome Back {username}!")
            return redirect(url_for("index"))
            # 
        else:
            flash("!Incorrect Password! Please Try Again!")
            return redirect(url_for("index"))
    else:
        # row = None
        flash(f"username {username} does not exists! please signup to create new account")
        return redirect(url_for("signup"))

@app.route("/mk_signup", methods=["POST"])
def mk_signup():
    first_name = escape(request.form["fname"]).lower().strip()
    last_name = escape(request.form["lname"]).lower().strip()
    email = escape(request.form["email"]).lower().strip()
    username = escape(request.form["uname"]).lower().strip()
    password = escape(request.form["password"])
    # email unique, username unique
    db, cursor = get_db()
    cursor.execute("SELECT * FROM user WHERE username=?", (username,))
    row = cursor.fetchone()
    # ("sachin", "sachin@gmail.com", "sachin", "yadav", "yahoo"), None
    if row:
        flash("!username already exists! please select another username!")
        return redirect(url_for("signup"))
    else:
        cursor.execute("SELECT * FROM user WHERE email=?", (email,))
        row = cursor.fetchone()
        if row:
            flash("!email already exists! please Login!")
        else:
            cursor.execute(
            "INSERT INTO user VALUES (?, ?, ?, ?, ?)", 
            (username, email, first_name, last_name, password))
            db.commit()
            close_db(db, cursor)
            flash("Account Created successfully! Please Login to Continue!")
    return redirect(url_for("index"))

@app.route("/show_all")
def show_all():
    db, cursor = get_db()
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    cursor.execute("SELECT * FROM city")
    city = cursor.fetchall()
    data = {"user": users, "city": city}
    close_db(db, cursor)
    return jsonify(data)

@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
        flash("!logout sucessfully!")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
    # host=localhost, port=5000
    # ASGI, WSGI, CGI
    # RBACK - admin
