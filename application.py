import mysql.connector
from flask import Flask
import json

app = Flask(__name__)


def get_db_connection():
    try:
        db = mysql.connector.connect(user="mysqlMaster", password="Master@123",
                                      host="watcherdatabse.mysql.database.azure.com", port=3306,
                                      database="watcherdatabse", ssl_ca="{ca-cert filename}", ssl_disabled=False)

        return db
    except Exception as e:
        print('DB connection error', e)
        return None


@app.route("/testDBConnection/")
def test_db_connection():
    db = get_db_connection()

    if db:
        my_cursor = db.cursor()
        my_cursor.execute("SELECT VERSION()")
        results = my_cursor.fetchone()
    else:
        results = None

    if results:
        return "DB connection successful"
    else:
        return "DB connection is unsuccessful"


@app.route("/getMostPopularTitles/")
def get_most_popular_titles():
    db = get_db_connection()

    try:
        if db:
            cursor = db.cursor()
            cursor.execute("select * from `watcherdatabse`.`MostPopularTitlesDaily`")
            row_headers = [x[0] for x in cursor.description]
            out_put = cursor.fetchall()

            json_data = []
            for result in out_put:
                json_data.append(dict(zip(row_headers, result)))
            return json.dumps(json_data, default=str)
        else:
            return ''

    except Exception as e:
        return "Ran into an exception while reading"



@app.route("/get/")
def hello():
    return "Hello World"


if __name__ == '__main__':
    app.run()
