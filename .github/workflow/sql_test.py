import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

try:
    conn = pymysql.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        db=os.getenv("db")
    )
    print("✅ MySQL connection successful!")
except Exception as e:
    print("❌ MySQL connection failed:", e)


