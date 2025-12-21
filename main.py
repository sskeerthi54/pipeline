from db_connector import get_postgres_connection

def main():
    conn = get_postgres_connection(
        dbname="myapp_db",
        user="postgres",
        password="postgres@123"
    )

    with conn.cursor() as cur:
        # 1. Create table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            );
        """)

        # 2. Insert 3 rows
        cur.execute("""
            INSERT INTO users (name, email)
            VALUES
                ('Alice', 'alice@example.com'),
                ('Bob', 'bob@example.com'),
                ('Charlie', 'charlie@example.com')
            ON CONFLICT DO NOTHING;
        """)

        # Commit changes
        conn.commit()

        print("Table created and data inserted successfully.\n")

        # 3. Extract table data
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()

        print("Users table data:")
        for row in rows:
            print(row)

    conn.close()

if __name__ == "__main__":
    main()
