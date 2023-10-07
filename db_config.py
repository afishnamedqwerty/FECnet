import psycopg2
from psycopg2 import extras
from cryptography.fernet import Fernet
import os

# Securely fetch database credentials
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')

def init_db(data):
    try:
        # Connect to PostgreSQL database with SSL
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            dbname=DB_NAME,
            sslmode='require'
        )
        
        cursor = conn.cursor(cursor_factory=extras.DictCursor)
        
        # Insert data
        # Assuming AES encryption is done on the data
        for entry in data:
            cursor.execute("INSERT INTO financial_data VALUES (%s, %s, %s, %s, %s)", (entry['office'], entry['candidate'], entry['total_receipts'], entry['donors'], entry['committee']))
        
        conn.commit()
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Database Error: {e}")
