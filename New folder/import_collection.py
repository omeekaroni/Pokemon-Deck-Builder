import csv
from database import get_connection
connection = get_connection()

cursor = connection.cursor()

with open("Collection.csv",
          newline="",
          encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        cursor.execute("""
        INSERT OR REPLACE INTO collection
        (
            card_name,
            quantity,
            regulation,
            set_code
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            row["Card Name"],
            int(row["Quantity"]),
            row["Regulation"],
            row["Set"]
        ))

connection.commit()

connection.close()

print("Collection Imported")