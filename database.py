import psycopg2
from settings import DATABASE_NAME, DATABASE_USER


def run_query(query, db_schema=DATABASE_NAME, db_username=DATABASE_USER):
    # Connect to an existing database
    conn = psycopg2.connect("dbname={} user={}".format(db_schema, db_username))

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute(query)
    data = cur.fetchall()


    # Close communication with the database
    cur.close()
    conn.close()
    return data