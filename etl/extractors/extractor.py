from etl.connectors.connector import get_postgres_connection

class UserExtractor:
    def extract(self, last_id=0):
        conn = get_postgres_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, name, email FROM users WHERE id > %s ORDER BY id",
                    (last_id,)
                )
                return cur.fetchall()
        finally:
            conn.close()