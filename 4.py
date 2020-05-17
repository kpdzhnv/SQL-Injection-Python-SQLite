import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def delete_secret(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the secret
    :return:
    """
    sql = 'DELETE FROM secrets WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_secrets(conn):
    """
    Delete all rows in the secrets table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM secrets'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    database = r"C:\Users\nica\Documents\studies\hack\lab-4\secrets.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        delete_all_secrets(conn);


if __name__ == '__main__':
    main()