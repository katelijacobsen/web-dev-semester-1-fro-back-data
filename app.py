from flask import Flask, flash, render_template, request, jsonify, g, session, redirect, url_for
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
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

Session(app) #what the hell was this used for again if we use session and not Session?


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

@app.route('/logout')
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
def api_login():
    try:
        user_email = config.validate_user_email()
        user_password = config.validate_user_password()
        db, cursor = config.db()


        q = "SELECT * FROM users WHERE user_email = %s"
        
        cursor.execute(q, (user_email,))
        
        user = cursor.fetchone()

        
        if not user: 
            error_msg = "Invalid credentials 001"
            tip = render_template("tip.html", status="error", msg=error_msg)
            return f"""<browser mix-after-begin="#tip">{tip}</browser>""", 400
        
        app.logger.info('expected = "%s", given = "%s" ________USER PASSWORD', user["user_password"], user_password)
        if not check_password_hash(user["user_password"], user_password):
            error_msg = "Invalid credentials 2"
            tip = render_template("tip.html", status="error", msg=error_msg)
            return f"""<browser mix-after-begin="#tip">{tip}</browser>""", 400
        
        user.pop("user_password")
        session["user_id"] = user["user_id"]
        
        return f"""<browser mix-redirect="/"></browser>"""    
            
    except Exception as ex: 
        ic(ex)
        
        if "company_exception user_email" in str(ex):
            error_msg = "Invalid credentials 02"
            tip = render_template("tip.html", status="error", msg=error_msg)
            return f"""<browser mix-after-begin="#tip">{tip}</browser>""", 400
        
        
        if "company_exception user_password" in str(ex):
            error_msg = "Invalid credentials 02"
            tip = render_template("tip.html", status="error", msg=error_msg)
            return f"""<browser mix-after-begin="#tip">{tip}</browser>""", 400
            
        
        error_msg = "Invalid credentials"
        tip = render_template("tip.html", status="error", msg=error_msg)
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
        user_country_id = request.form.get("user_country_id")
        user_password = config.validate_user_password()
        user_hashed_password = generate_password_hash(user_password)
        user_created_at = int(time.time())+3600
        
        db, cursor = config.db()
        q = "INSERT INTO users (user_id, user_username, user_first_name, user_last_name, user_email, user_phone, user_country_id, user_password, user_created_at) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(q, (user_id, user_username, user_first_name, user_last_name, user_email, user_phone, user_country_id, user_hashed_password, user_created_at))
        db.commit()
        
        signup = render_template("signup.html", config=config)
        
        # Send this user to login when sign up
        return f"""<browser mix-replace="form">{signup}</browser>
                <browser mix-redirect="/login"></browser>"""
        
    except Exception as ex:
        
        ic(ex)
        
        
        if "Duplicate entry" in str(ex) and "user_username" in str(ex):
            return f"""<browser mix-update="#username-error">Username already taken</browser>""", 400
        
        
        if "Duplicate entry" in str(ex) and "user_email" in str(ex):
            return f"""<browser mix-update="#email-error">Email already taken</browser>""", 400
        
        
        msg = str(ex) if ex.args else "System error"
        return f"""<browser mix-update="#tip">{msg}</browser>""", 500
    
    
    finally: 
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

#######################################################


@app.post('/api-create-recipie')
def upload_file():
    try:
        post_title = request.form.get('post_title') 
        post_description = request.form.get('post_description')
        
        
        file = request.files['recipe_file']
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

#######################################################

@app.delete('/api-delete-recipie')
def delete_post(recipie_id):
    try:
        cursor, db = config.db()
        q = ""
        cursor.execute(q, (recipie_id))
        db.commit()
    except Exception as ex:
        ic(ex)
        return "haha whoops", 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals(): db.close()


@app.patch('/')
def update_recipie():
    try:
        #TO DO VALIDATE SOME DATA
        cursor, db = config.db()
        #QUERY
        q = ""
    except Exception as ex: 
        ic(ex)
        #HANDLING ERRORRTYPES 
        return "haha whoops", 500
    finally: 
        # Worst handling scenarious
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

