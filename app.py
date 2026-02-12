from flask import Flask, render_template, request, jsonify
import connector
import uuid

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
        user_name = request.form.get("user_name")
        user_password = request.form.get("user_password")
        return "ok"
    except Exception as ex:
        pass
    finally:
        return "Didn't work, ay?", 500

#######################################################




####################### SIGN UP #######################
@app.post("/signup")
def create_user():
    try:
        #TODO: Validate data
        user_pk = uuid.uuid4().hex
        user_name = request.form.get("user_name")
        user_last_name = request.form.get("user_last_name")
        user_password = request.form.get("user_password")
        user_email = request.form.get("user_email")
        q = ""
        db,cursor = connector.db()
        cursor.execute(q, (user_pk, user_name, user_last_name, user_password, user_email))
        return jsonify({"id":user_pk})
    except Exception as ex:
        print(ex)
        return jsonify({"whoops . . . : Server error"}), 500
    finally:
        if "cursour" in locals(): cursor.close()
        if "db" in locals(): db.close()

#######################################################