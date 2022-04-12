from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_remote_data_base_connection():
    return mysql.connector.connection(
        host="129.146.128.174",
        port="3306",
        user="mysqlMaster",
        password="Master@123"
    )


def get_db_connection():
    try:
        db = get_remote_data_base_connection()
        my_cursor = db.cursor()
        my_cursor.excute("SELECT VERSION()")
        return my_cursor.fetchone()

    except Exception as e:
        print('DB connection error', e)
        return None


@app.route("/testDBConnection")
def test_db_connection():

    results = get_db_connection()

    if results:
        return "DB connection successful"
    else:
        return "DB connection is unsuccessful"

@app.route("/get/")
def hello():
    return "Hello World"


if __name__ == '__main__':
    app.run()

