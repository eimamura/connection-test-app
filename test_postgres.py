import os
from dotenv import load_dotenv
import psycopg2

def test_postgres_connection():
    # Load environment variables from the .env file
    load_dotenv()

    # Retrieve the secrets from environment variables
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    database = os.getenv("DATABASE")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")

    conn = None
    try:
        # Establish a connection to the remote PostgreSQL database
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute a sample query to check the connection
        cursor.execute("SELECT version()")

        # Fetch the result of the query
        result = cursor.fetchone()

        print("Connected to PostgreSQL successfully")
        print("PostgreSQL version:", result[0])

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except (psycopg2.Error, Exception) as e:
        print("Error connecting to PostgreSQL:", e)

# Call the function to test the connection
test_postgres_connection()
