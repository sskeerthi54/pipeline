import psycopg

def get_postgres_connection(
    dbname: str,
    user: str,
    password: str,
    host: str = "localhost",
    port: int = 5432
):
    """
    Returns a PostgreSQL connection
    """
    try:
        conn = psycopg.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("PostgreSQL connection successful")
        return conn
    except Exception as e:
        print("PostgreSQL connection failed")
        raise e
