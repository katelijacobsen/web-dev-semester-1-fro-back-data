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


@app.post('/api-create-recipe')
def create_recipe():
    try:
        recipe_title = config.validate_recipe_title()
        recipe_description = config.validate_recipe_description()
        recipe_servings = config.validation_recipe_servings()
        recipe_prep_time = request.form.get("recipe_prep_time")
        recipe_cook_time = request.form.get("recipe_cook_time")

        recipe_id = uuid.uuid4().hex
        user_id = session.get('user_id')
        if not user_id:
            return redirect("/login")

        file = request.files['recipe_file']
        file_key = f"{uuid.uuid4().hex}_{file.filename}"
        path = f"{UPLOAD_FOLDER}/{file_key}"

        db, cursor = config.db()

        # Insert recipe (no ingredients/instructions columns)
        q = """
        INSERT INTO recipes (
            recipe_id, user_id, recipe_title, recipe_img_key,
            recipe_description, recipe_prep_time, recipe_cook_time,
            recipe_servings, recipe_created_at
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(q, (
            recipe_id, user_id, recipe_title, file_key,
            recipe_description, recipe_prep_time, recipe_cook_time,
            recipe_servings, int(time.time())
        ))

        # Insert ingredients
        ingridient_names   = request.form.getlist("ingridient_name")
        ingridient_amounts = request.form.getlist("ingridient_amount")
        ingridient_units   = request.form.getlist("ingredient_unit")

        ic(ingridient_names)
        ic(ingridient_amounts)
        ic(ingridient_units)

        for name, amount, unit in zip(ingridient_names, ingridient_amounts, ingridient_units):
            ingridient_id = uuid.uuid4().hex
            cursor.execute(
                "INSERT INTO ingridients (ingridient_id, recipe_fk, ingridient_names, ingridient_amounts, ingridient_units) VALUES (%s, %s, %s, %s, %s)",
                (ingridient_id, recipe_id, name.strip(), amount.strip(), unit.strip())
            )

        # Insert instructions
        instructions = request.form.getlist("instructions")
        for step_number, instruction in enumerate(instructions, start=1):
            instruction_id = uuid.uuid4().hex
            cursor.execute(
                "INSERT INTO instructions (instruction_id, recipe_fk, instruction, instruction_step_number) VALUES (%s, %s, %s, %s)",
                (instruction_id, recipe_id, instruction.strip(), step_number)
            )
            
        ic(instructions)

        db.commit()
        # Save file only after successful DB commit
        file.save(path)

        return redirect(f"/")

    except Exception as ex:
        ic(ex)
        return f"""<browser mix-update="#tip">Error: {str(ex)}</browser>""", 500
    


    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals(): db.close()
#######################################################

@app.delete('/api-delete-recipe')
def delete_post(recipe_id):
    try:
        cursor, db = config.db()
        q = ""
        cursor.execute(q, (recipe_id))
        db.commit()
    except Exception as ex:
        ic(ex)
        return "haha whoops", 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals(): db.close()


@app.patch('/')
def update_recipe():
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

