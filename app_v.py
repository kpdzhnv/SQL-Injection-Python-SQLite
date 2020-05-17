from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app_v = Flask(__name__)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_secret_by_name_and_password(conn, name, password):
    """
    Query tasks by name
    :param conn: the Connection object
    :param name, password:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT secret FROM secrets WHERE name='%s' AND password='%s'" % (name, password))

    res = cur.fetchall()

    return res


@app_v.route("/", methods=["GET", "POST"])
def index():
    database = r"secrets.db"

    # create a database connection
    conn = create_connection(database)

    the_secret = "******"
    if request.method == "POST":
        user = request.form['username']
        password = request.form['password']
        with conn:
            the_secret = select_secret_by_name_and_password(conn, user, password)

    return render_template("index.html", secret=the_secret)


if __name__ == '__main__':
    app_v.run(debug=True)
