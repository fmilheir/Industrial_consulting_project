import psycopg2
from psycopg2 import pool
import random
import string


class DBPool:
    _instance = None

    @staticmethod
    def get_instance():
        if DBPool._instance is None:
            DBPool._instance = pool.ThreadedConnectionPool(minconn=1, maxconn=10,
                                                           user="postgres",
                                                           password="postgres",
                                                           host="postgresql",
                                                           port="5432",
                                                           database='industrial_consulting')
        return DBPool._instance

def create_table_user_if_not_exists():
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'user')")
            table_exists = cur.fetchone()[0]

            if not table_exists:
                cur.execute("""
                    CREATE TABLE "user" (
                        id SERIAL PRIMARY KEY,
                        first_name VARCHAR(255) NOT NULL,
                        last_name VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL UNIQUE,
                        number VARCHAR(20),
                        password VARCHAR(255) NOT NULL,
                        verification_code VARCHAR(6),
                        verified BOOLEAN NOT NULL DEFAULT FALSE,
                        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                conn.commit()
                return "Table 'user' created successfully."
            else:
                return "Table 'user' already exists."
        

def test_db_connection():
    conn = None
    try:
        conn = DBPool.get_instance().getconn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM test LIMIT 1")

        row = cur.fetchone()
        return f"Database connection successful. Test query result: {row} User table: {create_table_user_if_not_exists()}"
    except psycopg2.Error as e:
        return f"Unable to connect to the database: {e}"
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            DBPool.get_instance().putconn(conn)

def create_verification_code(size=6):
    return ''.join(random.choice(string.ascii_upercase + string.digits) for _ in range(size))



def store_user_in_database(first_name, last_name, email, phone_number, hashed_password):
    verfication_code = create_verification_code()
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "user" (first_name, last_name, email, number, password, verification_code, verified)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (first_name, last_name, email, phone_number, hashed_password, verfication_code, False))
            conn.commit()
            return "User stored successfully."
        

def verify_user_account(email, verification_code):
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            # Checking if the code matches 
            cur.execute("""
                        SELECT verification_code FROM "user" WHERE email = %s
                        """, (email,))
            stored_code = cur.fetchone()
            if stored_code and stored_code[0] == verification_code:
                # Updating the user's verification staus
                cur.execute("""
                            UPDATE "user" SET verified = %s WHERE email = %s
                            """, (True, email))
                conn.commit()
                return "User Verified successfully."
            else:
                return "Verification code does not match."
    
