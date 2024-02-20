import psycopg2
from psycopg2 import pool

class DBPool:
    _instance = None

    @staticmethod
    def get_instance():
        if DBPool._instance is None:
            DBPool._instance = pool.ThreadedConnectionPool(minconn=1, maxconn=10,
                                                           user="postgres",
                                                           password="postgres",
                                                           host="127.0.0.1",
                                                           port="5432",
                                                           database='industrial_consulting')
        return DBPool._instance

def create_table_user_if_not_exists():
    conn = None
    try:
        conn = DBPool.get_instance().getconn()
        cur = conn.cursor()

        cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'user')")
        table_exists = cur.fetchone()[0]

        if not table_exists:
            cur.execute("""
                CREATE TABLE "user" (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(255) NOT NULL,
                    last_name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    number VARCHAR(20)
                )
            """)
            conn.commit()
            return "Table 'user' created successfully."
        else:
            return "Table 'user' already exists."

    except psycopg2.Error as e:
        return f"Unable to create table: {e}"
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

def test_db_connection():
    conn = None
    try:
        conn = DBPool.get_instance().getconn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM test LIMIT 1")

        row = cur.fetchone()
        
        value = f"Database connection successful. Test query result: {row} User table: {create_table_user_if_not_exists()}"

        #Close connection after all queries
        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

        return value
    except psycopg2.Error as e:
        return f"Unable to connect to the database: {e}"
