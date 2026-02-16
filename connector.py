import mysql.connector

def db():
    try:
        db = mysql.connector.connect(
            host = "mariadb",
            user = "root",
            password = "password",
            database = "sign-up"
        )
        cursor = db.cursor(dictionary=True)
        return db, cursor
    except Exception as e:
        print(e, flush=True)
        raise Exception("Database under maintenance", 500)