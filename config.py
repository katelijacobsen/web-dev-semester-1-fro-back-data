from flask import request
import mysql.connector
import re # Regex

def db():
    try:
        db = mysql.connector.connect(
            host = "mariadb",
            user = "root",
            password = "password",
            database = "foodhead"
        )
        cursor = db.cursor(dictionary=True)
        return db, cursor
    except Exception as e:
        print(e, flush=True)
        raise Exception("Database under maintenance", 500)
    
#REGEX CONSTS###############
USER_NAME_MIN = 2
USER_NAME_MAX = 20
USER_PASSWORD_MIN = 8

REGEX_USER_NAME = f"^.{{{USER_NAME_MIN},{USER_NAME_MAX}}}$"
REGEX_USER_PASSWORD = f"^.{{{USER_PASSWORD_MIN},}}$"
###############REGEX CONSTS#

    
#VALIDATION FOR USER FIRST NAME###############

def validate_user_first_name():
    user_first_name = request.form.get("user_first_name").strip()
    if not re.match(REGEX_USER_NAME, user_first_name):
        raise Exception (f"-------error-------------- user_first_name")
    
    return user_first_name

###############VALIDATION FOR USER FIRST NAME#


#VALIDATION FOR USER LAST NAME###############

def validate_user_last_name():
    user_last_name = request.form.get("user_last_name")
    if not re.match(REGEX_USER_NAME, user_last_name):
        raise Exception(f"-------error-------------- user_last_name")
    
    return user_last_name

###############VALIDATION FOR USER LAST NAME#

#VALIDATION FOR USER USERNAME###############

def validate_user_username():
    user_username = request.form.get("user_username").strip()
    if not re.match(REGEX_USER_NAME, user_username):
        raise Exception(f"-------error-------------- user_username")
    
    return user_username


###############VALIDATION FOR USER USERNAME#

#VALIDATION FOR USER PASSWORD###############

def validate_user_password():
    user_password = request.form.get("user_password")
    confirm_password = request.form.get("confirm_password")
    
    if not user_password or not confirm_password:
        raise Exception("Password and confirmation are required")
    
    if user_password != confirm_password:
        raise Exception("Passwords do not match")
    
    if not re.match(REGEX_USER_PASSWORD, user_password):
        raise Exception(f"Password must be at least {USER_PASSWORD_MIN} characters long")
    
    return user_password

###############VALIDATION FOR USER PASSWORD#