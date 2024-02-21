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
                    id SERIAL PRIMARY KEY AUTO_INCREMENT,
                    first_name VARCHAR(255) NOT NULL,
                    last_name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    number VARCHAR(20),
                    admin INTEGER
                )
            """)
            conn.commit()

        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

        return "Table 'user' created successfully."

    except psycopg2.Error as e:
        return f"Unable to create table: {e}"


def create_table_car_if_not_exists():
    conn = None
    try:
        conn = DBPool.get_instance().getconn()
        cur = conn.cursor()

        cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'car')")
        table_exists = cur.fetchone()[0]

        if not table_exists:
            cur.execute("""
                CREATE TABLE "car" (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    reg VARCHAR(255) NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES "user"(id)
                )
            """)
            conn.commit()

        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

        return "Table 'car' created successfully."

    except psycopg2.Error as e:
        return f"Unable to create table 'car': {e}"

def create_table_trip_if_not_exists():
    conn = None
    try:
        conn = DBPool.get_instance().getconn()
        cur = conn.cursor()

        cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'trip')")
        table_exists = cur.fetchone()[0]

        if not table_exists:
            cur.execute("""
                CREATE TABLE "trip" (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    trip INTEGER NOT NULL,
                    footprint INTEGER NOT NULL,
                    car_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES "user"(id),
                    FOREIGN KEY (car_id) REFERENCES "car"(id)
                )
            """)
            conn.commit()

        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

        return "Table 'trip' created successfully."

    except psycopg2.Error as e:
        return f"Unable to create table 'trip': {e}"


def create_table_trip_if_not_exists():
    conn = None
    try:
        conn = DBPool.get_instance().getconn()
        cur = conn.cursor()

        cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'trip')")
        table_exists = cur.fetchone()[0]

        if not table_exists:
            cur.execute("""
                CREATE TABLE "trip" (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    distance INTEGER NOT NULL,
                    footprint INTEGER NOT NULL,
                    car_id INTEGER NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES "user"(id),
                    FOREIGN KEY (car_id) REFERENCES "car"(id)
                )
            """)
            conn.commit()

        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

        return "Table 'trip' created successfully."

    except psycopg2.Error as e:
        return f"Unable to create table 'car': {e}"


def create_table_public_transport_if_not_exists():
    conn = None
    try:
        conn = DBPool.get_instance().getconn()
        cur = conn.cursor()

        cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'public_transport')")
        table_exists = cur.fetchone()[0]

        if not table_exists:
            cur.execute("""
                CREATE TABLE "public_transport" (
                    id SERIAL PRIMARY KEY,
                    type VARCHAR(255),
                    footprint INTEGER NOT NULL
                )
            """)
            conn.commit()

        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

        return "Table 'public_transport' created successfully."

    except psycopg2.Error as e:
        return f"Unable to create table 'public_transport': {e}"

#Insert queries
def create_new_user(first_name, last_name, email, number, admin):
    conn = None
    try:
        conn = DBPool.get_instance().getconn()
        cur = conn.cursor()

        #psycopg2 sanitises inputs automatically so should be safe from SQL injections
        cur.execute("INSERT INTO user (first_name, last_name, email, number, admin) VALUES (%s, %s, %s, %s, %s)", (first_name, last_name, email, number, admin))
        conn.commit()

        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

        return "New user created successfully."

    except psycopg2.Error as e:
        return f"Unable to create new user: {e}"

def create_new_public_transport(transport_type, footprint):
    conn = None
    try:
        conn = DBPool.get_instance().getconn()
        cur = conn.cursor()

        #psycopg2 sanitises inputs automatically so should be safe from SQL injections
        cur.execute("INSERT INTO public_transport(type, footprint) VALUES (%s, %s)", (transport_type, footprint))
        conn.commit()

        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

        return "New transport created successfully."

    except psycopg2.Error as e:
        return f"Unable to create new user: {e}"



#Generic database connection test
def test_db_connection():
    conn = None
    try:
        conn = DBPool.get_instance().getconn()
        cur = conn.cursor()

        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

        return "Database connection successful"
    except psycopg2.Error as e:
        return f"Unable to connect to the database: {e}"
