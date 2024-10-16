import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect("whey.db")
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


if __name__ == "__main__":
    conn = create_connection("whey.db")
    create_table(conn, "CREATE TABLE IF NOT EXISTS whey (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date DATE NOT NULL, store TEXT NOT NULL, brand TEXT NOT NULL, name TEXT NOT NULL, taste TEXT NOT NULL, sku TEXT NOT NULL, price INTEGER NOT NULL)")
    conn.close()