from database import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS collection (

    card_name TEXT PRIMARY KEY,

    quantity INTEGER,

    regulation TEXT,

    set_code TEXT

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS wishlist (

    card_name TEXT PRIMARY KEY,

    needed_quantity INTEGER

)
""")

connection.commit()

connection.close()

print("Database Created")