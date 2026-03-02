from flask import Flask, render_template, request, jsonify, g, session, redirect, url_for
from icecream import ic

import config
import uuid
import time

ic.configureOutput(prefix=f"________________________________|  '", includeContext=True)

app = Flask(__name__)
# secret key to protect data
app.secret_key = b'smashkeyboarded123'



#ic( int(time.time())+3600)

@app.before_request
def load_user():
    user_id = session.get("user_id")
    if user_id:
        db, cursor = config.db()
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

    return render_template("signup.html", config=config)

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
        db, cursor = config.db()
        cursor.execute(q, (given_email,))
        user = cursor.fetchone()
        #error handling if login doesn't match in the db
        if user is None or given_password !=user["user_password"]:
            return render_template("login.html", error="Invalid email or password")
        
        # using session to store the login
        session["user_id"] = user['user_id']
        session["user_username"] = user['user_username']

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
    db, cursor = config.db()
    cursor.execute(q, ())
    users = cursor.fetchall()
    return jsonify(users)

####################### SIGN UP #######################

@app.post("/signup")
def signup_post():
    try:
        ic("***************************************************")
        #TODO: Validate data
        user_id  = uuid.uuid4().hex
        user_username = config.validate_user_username()
        user_first_name = config.validate_user_first_name()
        user_last_name = config.validate_user_last_name()
        country = request.form.get("country")
        user_tel = request.form.get("user_tel")
        user_password = config.validate_user_password()
        user_email = request.form.get("user_email")
        user_created_at = int(time.time())+3600
        ic(user_created_at)
        #query
        q = "INSERT INTO users (user_id, user_username, user_first_name, user_last_name, country, user_email, user_tel, user_password, user_created_at) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        db,cursor = config.db()
        # execute the query with the data
        cursor.execute(q, (user_id, user_username, user_first_name, user_last_name, country, user_email, user_tel, user_password, user_created_at))
        # commit the transactionF
        db.commit()
        return render_template("complete.html")
    except Exception as ex:
        # handle error 
        if "Duplicate entry" in str(ex) and "user_username" in str(ex):
            return "username is already taken", 400
        error_msg = str(ex) if ex.args else "Server error"
        return error_msg, 500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()
        
#######################################################

@app.post("/api-check-user")
def check_user(): 
    try:
        user_username = config.validate_user_username()
        db, cursor = config.db()
        
        q = "SELECT * FROM users WHERE user_username = %s"
        cursor.execute(q, (user_username,))
        row = cursor.fetchone()
        if not row:
            return f"""<browser mix-update="span">Username is avaiable</browser>""" 
        
        return f"""<browser mix-update="span">Username is taken</browser>""" 
    
    except Exception as ex:
        ic(ex)
        if "-------error-------------- user_username" in str(ex):
            return f"""<browser mix-update="span">Invalid username</browser>""", 400
        return f"""<browser mix-update="span">System error</browser>""", 500
             
        
    finally: 
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close() 

#######################################################
#######################################################

@app.post("/api-create-user")
def create_user(): 
    try:
        user_id = uuid.uuid4().hex
        user_username = config.validate_user_username()
        user_first_name = config.validate_user_first_name()
        user_last_name = config.validate_user_last_name()
        user_email = request.form.get("user_email")
        user_tel = request.form.get("user_tel")
        country = request.form.get("country")
        user_password = config.validate_user_password()
        user_created_at = int(time.time())+3600
        
        db, cursor = config.db()
        q = "INSERT INTO users (user_id, user_username, user_first_name, user_last_name, user_email, user_tel, country, user_password, user_created_at) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(q, (user_id, user_username, user_first_name, user_last_name, user_email, user_tel, country, user_password, user_created_at))
        db.commit()
        
        tip = render_template("tooltip.html", msg="Sign up complete")
        return f"""<browser mix-update="#tooltip">{tip}</browser>"""
        
    except Exception as ex:
        ic(ex)
        if "Duplicate entry" in str(ex) and "user_username" in str(ex):
            return f"""<browser mix-update="#tooltip">Username already taken</browser>""", 400
        msg = str(ex) if ex.args else "System error"
        return f"""<browser mix-update="#tooltip">{msg}</browser>""", 500
    finally: 
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

#######################################################