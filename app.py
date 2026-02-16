from flask import Flask, render_template, request, jsonify
import connector
import uuid
import random

app = Flask(__name__)

########################ROUTING#########################

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/signup.html")
def signup():
    return render_template("signup.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

#######################################################


####################### LOGIN #########################

@app.get("/login/<user_pk>")
def login_user(user_pk):
    try:
        user_pk = request.form.get("user_pk")
        user_name = request.form.get("user_name")
        user_password = request.form.get("user_password")
        return "ok"
    except Exception as ex:
        pass
    finally:
        return "Didn't work, ay?", 500

#######################################################

@app.get("/users")
def get_users():
    q = "SELECT * FROM users"
    db, cursor = connector.db()
    cursor.execute(q, ())
    users = cursor.fetchall()
    return jsonify(users)

####################### SIGN UP #######################
@app.post("/signup")
def create_user():
    try:
        #TODO: Validate data
        user_id  = uuid.uuid4().hex
        user_name = request.form.get("user_name")
        user_last_name = request.form.get("user_last_name")
        country = request.form.get("country")
        user_tel = request.form.get("user_tel")
        user_password = request.form.get("user_password")
        user_email = request.form.get("user_email")
        q = "INSERT INTO users (user_name, user_last_name, country, user_email, user_tel, user_password) VALUES(%s, %s, %s, %s, %s, %s)"
        db,cursor = connector.db()
        cursor.execute(q, (user_name, user_last_name, country, user_email, user_tel, user_password))
        db.commit()
        return render_template("complete.html")
    except Exception as ex:
        print(ex)
        return jsonify({"Msg": "server error", "error":str(ex)}), 500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()
        

#######################################################