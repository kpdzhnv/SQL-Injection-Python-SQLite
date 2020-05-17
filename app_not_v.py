from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app_not_v = Flask(__name__)


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


def select_secret_by_name(conn, name):
    """
    Query tasks by name
    :param conn: the Connection object
    :param name:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM secrets WHERE name=?", (name,))

    rows = cur.fetchall()

    return rows[0]


@app_not_v.route("/", methods=["GET", "POST"])
def index():
    database = r"secrets.db"

    # create a database connection
    conn = create_connection(database)

    showing_secret = "******"
    if request.method == "POST":
        user = request.form['username']
        password = request.form['password']
        with conn:
            the_secret = select_secret_by_name(conn, user)
        correct_password = the_secret[2]
        if password == correct_password:
            showing_secret = the_secret[3]

    return render_template("index.html", secret=showing_secret)


if __name__ == '__main__':
    app_not_v.run(debug=True)
