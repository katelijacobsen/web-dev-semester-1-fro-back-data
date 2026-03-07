from flask import Flask, flash, render_template, request, jsonify, g, session, redirect, url_for
from flask_session import Session
from icecream import ic

import config
import uuid
import time

UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

ic.configureOutput(prefix=f"________________________________|  '", includeContext=True)


app = Flask(__name__)
# secret key to protect data
#app.secret_key = b'smashkeyboarded123'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1000 * 1000

Session(app)


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
def signup_post():
    try:
        user = session.get("user", "")
        return render_template("signup.html", user=user, config=config)
    except Exception as ex:
        ic(ex)
        return "Haha whoops probably a type error. Have a nice day. Go touch some grass", 500


@app.get("/login")
def login():
    try:
        user = session.get("user", "")
        if not user: #if they are not login then show login page
            return render_template("login.html")
        return redirect("profile") #show profile for users that are logged in
    except Exception as ex:
        ic(ex)
        return "whoops" # of course "best case" scenario :^)

@app.route('/logout.html')
def logout():
    try:
        session.clear()
        return redirect("/login")
    except Exception as ex: 
        ic(ex)
        return "haha u can't figure out to logout. sad."

@app.route("/create")
def create_post():
    return render_template("create.html")

########################ERROR HANDLER#########################

#@app.errorhandler(404)
#def page_not_found(error):
#    return render_template("/"), 404

#######################################################


####################### LOGIN #########################

@app.post("/api-login")
def login_user():
    try:
        given_email = config.validate_user_email()
        given_password = config.validate_user_email()

        #app.logger.info('%s %s', given_password, given_email) #screw you flask
        
        # get db
        db, cursor = config.db()
        #query
        q = "SELECT * FROM users WHERE user_email = %s"
        
        cursor.execute(q, (given_email,))
        user = cursor.fetchone()
        
        #error handling if login doesn't match 
        if not user or not given_password(user["given_password"], given_password): 
            error_msg = "The email or password you entered is incorrect"
            tip = render_template("/tip.html", msg=error_msg)
            return f"""<browser mix-after-begin="#tooltip">{tip}</browser> """, 400
        
        user.pop("given_password")
        session["user"] = user
        
        return f"""<browser mix-redirect="/profile"></browser>"""
    
    except Exception as ex: 
        ic(ex)
        
        if not user or not given_password(user["given_password"], given_password): 
            error_msg = "The email or password you entered is incorrect"
            tip = render_template("/tip.html", msg=error_msg)
            return f"""<browser mix-after-begin="#tooltip">{tip}</browser> """, 400
        
        
        
        # Of course best case scenario :)
        error_msg = "System under maintenance"
        tip = render_template("tip.html", status="error", msg = error_msg)        
        return f"""<browser mix-after-begin="#tip">{tip}</browser>""", 500
    
    
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
            return f"""<browser mix-update="span">Avaiable</browser>""" 
        
        return f"""<browser mix-update="span">Username or email is taken</browser>""" 
    
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
        user_phone = request.form.get("user_tel")
        country = request.form.get("country")
        user_password = config.validate_user_password()
        user_created_at = int(time.time())+3600
        
        db, cursor = config.db()
        q = "INSERT INTO users (user_id, user_username, user_first_name, user_last_name, user_email, user_phone, country, user_password, user_created_at) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(q, (user_id, user_username, user_first_name, user_last_name, user_email, user_phone, country, user_password, user_created_at))
        db.commit()
        
        tip = render_template("tooltip.html", msg="Sign up complete")
        return f"""<browser mix-update="#tooltip">{tip}</browser>"""
        
    except Exception as ex:
        ic(ex)
        if "Duplicate entry" in str(ex) and "user_username" in str(ex):
            return f"""<browser mix-update="#user_">Username already taken</browser>""", 400
        if "Duplicate entry" in str(ex) and "user_email" in str(ex):
            return f"""<browser mix-update="#user_email_error">Email already taken</browser>""", 400
        msg = str(ex) if ex.args else "System error"
        return f"""<browser mix-update="#tooltip">{msg}</browser>""", 500
    finally: 
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

#######################################################

@app.post('/api-create-post')
def upload_file():
    try:
        post_title = request.form.get('post_title')
        post_description = request.form.get('post_description')
        
        
        file = request.files['file']
        file_key = f"{uuid.uuid4().hex}_{file.filename}"
        path = f"{UPLOAD_FOLDER }/{file_key}"
        file.save(path)
        
        #creating object
        post = {
            'post_id': uuid.uuid4().hex,
            'user_id': session['user_id'], #dictionary w/key
            'post_title': post_title,
            'post_img_key': file_key,
            'post_description': post_description,
            'post_created_at': int(time.time())+3600
        }
        
        db, cursor = config.db()
        q = """
        INSERT INTO posts (
            post_id,
            user_id,
            post_title,
            post_img_key,
            post_description,
            post_created_at
        ) VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        cursor.execute(q, (
            post["post_id"],
            post["user_id"],
            post["post_title"],
            post["post_img_key"],
            post["post_description"],
            post["post_created_at"]
        ))
        
        return render_template("index.html", post=post)
    
    except Exception as ex: 
        ic(ex)
        return jsonify({"Msg": "server error", "error":str(ex)}), 500 
    finally: 
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals(): db.close()


