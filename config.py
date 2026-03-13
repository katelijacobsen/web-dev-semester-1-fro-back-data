from flask import request, make_response
from functools import wraps # use decorator so the function knows automatically not to cache
import mysql.connector
import re # Regex


#_____REGEX CONSTS_____###############
USER_NAME_MIN = 2 #for this project I'll only use one type for validating names
USER_NAME_MAX = 20 #I'm too lazy to write more
USER_PASSWORD_MIN = 8
USER_PASSWORD_MAX = 20

RECIPE_TITLE_MIN = 2
RECIPE_TITLE_MAX = 50

RECIPE_DESCRIPTION_MIN = 50
RECIPE_DESCRIPTION_MAX = 500

RECIPE_INSTRUCTIONS_MIN = 100
RECIPE_INSTRUCTIONS_MAX = 500

RECIPE_INGRIDIENTS_MAX = 30

RECIPE_STEPS_MAX = 30


#__fuuuuuusion
REGEX_USER_EMAIL = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
REGEX_USER_NAME = f"^.{{{USER_NAME_MIN},{USER_NAME_MAX}}}$"
REGEX_USER_PASSWORD = f"^.{{{USER_PASSWORD_MIN},{USER_PASSWORD_MAX}}}$"
REGEX_RECIPE_TITLE = f"^.{{{RECIPE_TITLE_MIN},{RECIPE_TITLE_MAX}}}"
REGEX_RECIPE_INSTRUCTIONS = f"^.{{{RECIPE_INSTRUCTIONS_MIN},{RECIPE_INSTRUCTIONS_MAX}}}"
REGEX_RECIPE_DESCRIPTION = f"^.{{{RECIPE_DESCRIPTION_MIN},{RECIPE_DESCRIPTION_MAX}}}"
REGEX_RECIPE_SERVINGS = f"^(10|[1-9])$"
###############_____REGEX CONSTS_____#


#_____CONNECT TO DB_____##############################

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

##############################_____CONNECT TO DB_____#


    
#_____NO CACHE_____###################################

def no_cache(view):
    @wraps(view)
    def no_cache_view(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    return no_cache_view

###################################_____NO CACHE_____#

    
    
#_____VALIDATION FOR USER FIRST NAME_____###############

def validate_user_first_name():
    user_first_name = request.form.get("user_first_name").strip()
    if not re.match(REGEX_USER_NAME, user_first_name):
        raise Exception (f"____whoops user_first_name")
    
    return user_first_name

###############_____VALIDATION FOR USER FIRST NAME_____#


#_____VALIDATION FOR USER LAST NAME_____###############

def validate_user_last_name():
    user_last_name = request.form.get("user_last_name").strip()
    if not re.match(REGEX_USER_NAME, user_last_name):
        raise Exception(f"____whoops user_last_name")
    
    return user_last_name

###############_____VALIDATION FOR USER LAST NAME_____#



#_____VALIDATION FOR USER USERNAME_____###############

def validate_user_username():
    user_username = request.form.get("user_username").strip()
    if not re.match(REGEX_USER_NAME, user_username):
        raise Exception(f"____whoops user_username")
    
    return user_username


###############_____VALIDATION FOR USER USERNAME_____#



#_____VALIDATION FOR USER PASSWORD_____###############

def validate_user_password():
    user_password = request.form.get("user_password", "").strip()
    # if user didn't add password
    if not user_password:
        raise Exception("INVALID_PASSWORD user_password")
    
    #if password does not live up to the expectations
    if not re.match(REGEX_USER_PASSWORD, user_password):
        raise Exception(f"Password must be at least {USER_PASSWORD_MIN} characters long")
    
    return user_password

###############_____VALIDATION FOR USER PASSWORD_____#

#_____VALIDATION FOR USER EMAIL_____###################


def validate_user_email():
    user_email = request.form.get("user_email", "").strip() # use strip() to avoid spacing from left- and right side of the input
    if not re.match(REGEX_USER_EMAIL, user_email):
        raise Exception("INVALID_EMAIL user_email")
    return user_email

###################_____VALIDATION FOR USER EMAIL_____#



#_____VALIDATION FOR CREATING RECIPE_____###################

def validate_recipe_title():
    recipe_title = request.form.get("recipie_title", "").strip()
    if not re.match(REGEX_RECIPE_TITLE, recipe_title):
        raise Exception("foodhead recipe_title")
    return recipe_title


def validate_recipe_description():
    recipe_description = request.form.get("recipe_description", "").strip()
    if not re.match( REGEX_RECIPE_DESCRIPTION ,recipe_description):
        raise Exception("foodheadn recipe_description")


def validation_recipe_servings():
    recipe_servings = request.form.get("recipe_servings", "").strip()
    if not re.match(REGEX_RECIPE_SERVINGS, recipe_servings):
        raise Exception("foodhead recipe_servings")
    return recipe_servings

def validation_recipe_instructions():
    recipe_instruction = request.form.get("recipe_instruction", "").strip()
    if not re.match(REGEX_RECIPE_INSTRUCTIONS, recipe_instruction):
        raise Exception("foodhead recipe_instruction")
    return recipe_instruction
    
###################_____VALIDATION FOR CREATING RECIPE_____#