import psycopg2
from psycopg2 import pool
import jwt
import datetime
import logging
import os
from dotenv import load_dotenv

logger = logging.getLogger(__name__) 
load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET') or 'secret'
# DATABASE_URL = os.getenv("DATABASE_URL")

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
    try:
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
                            verification_token VARCHAR(255),
                            token_expiration TIMESTAMP,
                            verified BOOLEAN NOT NULL DEFAULT FALSE,
                            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
                    """)
                    conn.commit()
                    return "Table 'user' created successfully."
                else:
                    return "Table 'user' already exists."
    except psycopg2.Error as e:
        return f"Unable to create table: {e}"

            
def generate_jwt_token(email):
    try:
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        token = jwt.encode({'email': email, 'exp': expiration_time}, JWT_SECRET, algorithm='HS256')
        # Ensure the token is a string
        token = token.decode('utf-8') if isinstance(token, bytes) else token
        print("Verification token generated:", token)
        return token
    except Exception as e:
        print("Error generating JWT token:", str(e))
        return None





def store_user_in_database(first_name, last_name, email, phone_number, hashed_password, verification_token):
    token_expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    INSERT INTO "user" (first_name, last_name, email, number, password, verification_token, token_expiration, verified)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (first_name, last_name, email, phone_number, hashed_password, verification_token, token_expiration, False))
                if not phone_number.isdigit() or len(phone_number) != 10:
                    conn.rollback()
                    return "Invalid phone number format.", 400  # Bad Request
                conn.commit()
                print("User stored with verification token:", verification_token)
                return "User stored successfully."
            except psycopg2.errors.UniqueViolation as e:
                logger.error("Duplicate email address", exc_info=True)
                return "Failed to insert user: Email address already exists.", 409
            except psycopg2.Error as e:
                logger.error(f"Failed to insert user: {e}", exc_info=True)  # Log the error with stack trace
                # Rollback the transaction on error
                conn.rollback() 
                return f"Failed to insert user:", 500
            except Exception as e:
                logger.exception(f"Unexpected error: {e}")  # Log unexpected errors with full context 
                # Rollback the transaction on error
                conn.rollback() 
                return f"Unexpected error: {e}", 500
        

def verify_user_account(email, verification_token):
    with DBPool.get_instance().getconn() as conn:
        with conn.cursor() as cur:
            # Checking if the code matches 
            cur.execute("""
                        SELECT verification_token, token_expiration FROM "user" WHERE email = %s
                        """, (email,))
            stored_code = cur.fetchone()
            if stored_code: 
                stored_token, expiration_time = stored_code 
                if stored_token == verification_token and datetime.datetime.now() < expiration_time:
                    # Updating the user's verification status
                    cur.execute("""
                        UPDATE "user" SET verified = %s WHERE email = %s
                            """, (True, email))
                    conn.commit()
                    return "User Verified successfully."
                else:
                    return "Verification token expired or invalid."
            else:
                return "User not found."
