# which place to connect
# ** why use and name
#what is the output
import psycopg
from etl.config.config import DB_CONFIG


def get_postgres_connection():
    try:
        return psycopg.connect(**DB_CONFIG)
    except Exception as e:
        print("PostgreSQL connection failed")
        raise e
