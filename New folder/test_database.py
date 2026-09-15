from database import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute("""
SELECT *
FROM collection
""")

cards = cursor.fetchall()

for card in cards:
    print(card)

connection.close()