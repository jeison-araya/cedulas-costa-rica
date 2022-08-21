"""
Database configuration
"""
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def get_database():
    """
    Get database connection.
    """
    client = MongoClient(os.environ["MONGODB_URL"])
    db_name = os.environ.get("DB_NAME", "padron")

    return client[db_name]


database = get_database()
