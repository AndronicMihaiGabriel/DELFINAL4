import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()


def get_connection():
    conn_str = (
        f"DRIVER={{{os.getenv('DB_DRIVER')}}};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_DATABASE')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        f"Encrypt={os.getenv('DB_ENCRYPT')};"
        f"TrustServerCertificate={os.getenv('DB_TRUST_CERTIFICATE')};"
        f"Connection Timeout={os.getenv('DB_TIMEOUT')};"
    )
    return pyodbc.connect(conn_str)
