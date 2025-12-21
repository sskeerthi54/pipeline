from db_connector import get_postgres_connection
from config import DB_CONFIG


def extract_users():
    # Create DB connection using config
    conn = get_postgres_connection(
        dbname=DB_CONFIG["dbname"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"]
    )

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, email FROM users;")
            rows = cur.fetchall()

            print(" Extracted users data:")
            for row in rows:
                print(row)

    except Exception as e:
        print(" Error while extracting data")
        raise e

    finally:
        conn.close()
        print(" Connection closed")


if __name__ == "__main__":
    extract_users()
