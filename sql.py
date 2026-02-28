import sqlite3

def create_database():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        region TEXT,
        sales_amount INTEGER
    )
    """)

    # Insert sample data
    data = [
        ("Laptop", "North", 50000),
        ("Mobile", "South", 30000),
        ("Tablet", "East", 20000),
        ("Laptop", "West", 45000),
        ("Mobile", "North", 35000),
        ("Tablet", "South", 25000)
    ]

    cursor.executemany("""
        INSERT INTO sales (product_name, region, sales_amount)
        VALUES (?, ?, ?)
    """, data)

    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__ == "__main__":
    create_database()
