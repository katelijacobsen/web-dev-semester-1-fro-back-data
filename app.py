from flask import Flask, render_template, request, jsonify, g, session, redirect, url_for
from icecream import ic

import connector
import uuid
import time

ic.configureOutput(prefix=f"________________________________|  '", includeContext=True)

app = Flask(__name__)
# secret key to protect data
app.secret_key = b'smashkeyboarded123'

@app.before_request
def load_user():
    user_id = session.get("user_id")
    if user_id:
        db, cursor = connector.db()
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        # using g to globally handling request & for db connection
        g.user = cursor.fetchone()
        cursor.close()
        db.close()
    else:
        g.user = None

########################ROUTING#########################

@app.route("/")
def index():
    if g.user:
        return render_template("index.html", user=g.user) #use this in base.html
    return render_template("index.html")

@app.get("/signup")
def signup():
    try: 
        #TODO Validate data
        pass
    except Exception as ex:
        pass
    finally:
        pass
        #if "cursor" in locals(): cursor.close()
        #if "db" in locals(): db.close()

    return render_template("signup.html", conncector=connector)

@app.get("/login.html")
def login():
    return render_template("login.html")

@app.route('/logout.html')
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/create.html")
def create_post():
    return render_template("create.html")

########################ERROR HANDLER#########################

#@app.errorhandler(404)
#def page_not_found(error):
#    return render_template("/"), 404

#######################################################


####################### LOGIN #########################

@app.post("/login")
def login_user():
    try:
        given_email = request.form.get("email")
        given_password = request.form.get("password")

        #app.logger.info('%s %s', given_password, given_email) #screw you flask
        #query
        q = "SELECT * FROM users WHERE user_email = %s"
        db, cursor = connector.db()
        cursor.execute(q, (given_email,))
        user = cursor.fetchone()
        #error handling if login doesn't match in the db
        if user is None or given_password !=user["user_password"]:
            return render_template("login.html", error="Invalid email or password")
        
        # using session to store the login
        session["user_id"] = user['user_id']
        session["user_name"] = user['user_name']

        return redirect(url_for("index"))
    except Exception as ex: 
        print(ex)
        return jsonify({"Msg": "server error", "error":str(ex)}), 500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

#######################################################
# Checking if the I'm connected to the db
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
        user_username = connector.validate_user_username()
        user_first_name = connector.validate_user_first_name()
        user_last_name = connector.validate_user_last_name()
        country = request.form.get("country")
        user_tel = request.form.get("user_tel")
        user_password = request.form.get("user_password")
        user_email = request.form.get("user_email")
        #query
        q = "INSERT INTO users (user_id, user_username, user_last_name, country, user_email, user_tel, user_password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        db,cursor = connector.db()
        # execute the query with the data
        cursor.execute(q, (user_id, user_username, user_first_name, user_last_name, country, user_email, user_tel, user_password))
        # lol forgot this one
        db.commit()
        return render_template("complete.html")
    except Exception as ex:
        # handle error 
        if "Duplicate entry" in str(ex) and "user_username" in str(ex):
            return "username is already taken", 400
        return ex.args[0], ex.args[1]
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()
        
#######################################################

@app.post("/api-check-user")
def check_user(): 
    try:
        user_username = connector.validate_user_username()
        db, cursor = connector.db()
        
        q = "SELECT * FROM users WHERE user_username = %s"
        cursor.execute(q, (user_username,))
        row = cursor.fetchone()
        if not row:
            return f"""<browser mix-update="span">Username is avaiable</browser>""" 
        
        return f"""<browser mix-update="span">Username is taken</browser>""" 
    
    except Exception as ex:
        ic(ex)
        
        if "-----error--- user_username" in str(ex):
            return f"""<browser mix-update="span">{ex.args[0]}</browser>""",400
        return f"""<browser mix-update="span">System whoops</browser>""", 500
             
        
    finally: 
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close() 

#######################################################
#######################################################

@app.post("/api-create-user")
def create_user(): 
    try:
        pass
    except Exception as ex:
        pass
    finally: 
        pass

#######################################################