import psycopg2
import os
from dotenv import load_dotenv
# Define connection credentials

load_dotenv()


db_params = {
    "host": os.getenv("HOST"),
    "database": os.getenv("DATABASE"),
    "user": os.getenv("USERNAME"),
    "password": os.getenv("PASSWORD"),
    "port": os.getenv("PORT")  # 5432 is the default PostgreSQL port
}


try:
        # 1. Establish the connection
        with psycopg2.connect(**db_params) as conn:
            print("Connection to PostgreSQL successful!")
            
            # 2. Open a cursor to perform database operations
            with conn.cursor() as cursor:
                
                # 3. Execute a query
                cursor.execute("SELECT version();")
                
                # 4. Fetch results
                db_version = cursor.fetchone()
                print(f"PostgreSQL version: {db_version[0]}")
                
except Exception as error:
        print(f"Error connecting to database: {error}")
        
