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


def create_secret(conn, secret):
    """
    Create a new project into the projects table
    :param conn:
    :param secret:
    :return: secret id
    """
    sql = ''' INSERT INTO secrets(name,password,secret)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, secret)
    return cur.lastrowid


def main():
    database = r"C:\Users\nica\Documents\studies\hack\lab-4\secrets.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new secret
        secret_1 = ('Alice', 'qwerty', '523647');
        secret_1_id = create_secret(conn, secret_1)
        secret_2 = ('Bob', '1234', '846902');
        secret_2_id = create_secret(conn, secret_2)
        secret_3 = ('Candace', 'psswrd', '134798');
        secret_3_id = create_secret(conn, secret_3)
        secret_4 = ('Don', 'psswrd', '134798');
        secret_4_id = create_secret(conn, secret_4)
        secret_5 = ('Emma', 'psswrd', '134798');
        secret_5_id = create_secret(conn, secret_5)



if __name__ == '__main__':
    main()