import sqlite3


def get_connection():
    return sqlite3.connect("pokemon.db")


def get_all_cards():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            card_name,
            quantity,
            regulation,
            set_code
        FROM collection
        ORDER BY card_name
    """)

    cards = cursor.fetchall()

    connection.close()

    return cards


def get_card(card_name):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM collection
        WHERE card_name = ?
    """,
    (card_name,))

    card = cursor.fetchone()

    connection.close()

    return card


def add_card(
    card_name,
    quantity,
    regulation,
    set_code
):

    connection = get_connection()
    cursor = connection.cursor()

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
        card_name,
        quantity,
        regulation,
        set_code
    ))

    connection.commit()
    connection.close()


def update_quantity(
    card_name,
    quantity
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE collection
        SET quantity = ?
        WHERE card_name = ?
    """,
    (
        quantity,
        card_name
    ))

    connection.commit()

    rows = cursor.rowcount

    connection.close()

    return rows


def delete_card(card_name):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM collection
        WHERE card_name = ?
    """,
    (card_name,))

    connection.commit()

    rows = cursor.rowcount

    connection.close()

    return rows

def get_cards_by_regulation(regulation):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            card_name,
            quantity,
            set_code
        FROM collection
        WHERE regulation = ?
        ORDER BY card_name
    """,
    (regulation,))

    cards = cursor.fetchall()

    connection.close()

    return cards


def get_cards_by_set(set_code):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            card_name,
            quantity,
            regulation
        FROM collection
        WHERE set_code = ?
        ORDER BY card_name
    """,
    (set_code,))

    cards = cursor.fetchall()

    connection.close()

    return cards


def get_wishlist():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            card_name,
            needed_quantity
        FROM wishlist
        ORDER BY needed_quantity DESC
    """)

    cards = cursor.fetchall()

    connection.close()

    return cards

def clear_wishlist():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM wishlist
    """)

    connection.commit()
    connection.close()

def add_wishlist_card(
    card_name,
    quantity
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO wishlist
        (
            card_name,
            needed_quantity
        )
        VALUES (?, ?)
    """,
    (
        card_name,
        quantity
    ))

    connection.commit()
    connection.close()