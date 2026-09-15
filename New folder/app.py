import csv
import os
from database import get_connection
from database import (
    clear_wishlist,
    add_wishlist_card
)

def load_cards(filename):

    cards = {}

    with open(filename, newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            card_name = row["Card Name"]

            cards[card_name] = {
                "quantity": int(row["Quantity"]),
                "regulation": row["Regulation"],
                "set": row["Set"]
            }

    return cards

def load_collection_from_db():

    collection = {}

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            card_name,
            quantity,
            regulation,
            set_code
        FROM collection
    """)

    rows = cursor.fetchall()

    connection.close()

    for row in rows:

        collection[row[0]] = {
            "quantity": row[1],
            "regulation": row[2],
            "set": row[3]
        }

    return collection

def load_deck_csv(filename):

    cards = {}

    with open(filename, newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            cards[row["Card Name"]] = int(
                row["Quantity"]
            )

    return cards


def load_limitless_deck(filename):

    deck = {}

    with open(filename, encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            if ":" in line:
                continue

            parts = line.split()

            if not parts[0].isdigit():
                continue

            quantity = int(parts[0])

            card_name = " ".join(parts[1:-2])

            deck[card_name] = quantity

    return deck


def compare_deck(collection, deck):

    missing_cards = {}

    for card, required_qty in deck.items():

        owned_qty = collection.get(
            card,
            {"quantity": 0}
        )["quantity"]

        if owned_qty < required_qty:
            missing_cards[card] = required_qty - owned_qty

    required_total = sum(deck.values())
    missing_total = sum(missing_cards.values())

    completion = (
        (required_total - missing_total)
        / required_total
    ) * 100

    return completion, missing_cards

def run_deck_analyzer():

    collection = load_collection_from_db()

    print("Collection Summary")
    print("------------------")

    unique_cards = len(collection)

    total_cards = sum(
        card_data["quantity"]
        for card_data in collection.values()
    )

    print(f"Unique Cards: {unique_cards}")
    print(f"Total Cards: {total_cards}")
    print()

    print("Most Owned Cards")
    print("----------------")

    sorted_cards = sorted(
        collection.items(),
        key=lambda x: x[1]["quantity"],
        reverse=True
    )

    for card, data in sorted_cards[:5]:
        print(f"{card}: {data['quantity']}")

    print()

    regulation_counts = {}

    for card_data in collection.values():

        regulation = card_data["regulation"]

        if regulation not in regulation_counts:
            regulation_counts[regulation] = 0

        regulation_counts[regulation] += card_data["quantity"]

    print("Regulation Breakdown")
    print("--------------------")

    print("Cards By Regulation")
    print("-------------------")

    regulation_cards = {}

    for card_name, card_data in collection.items():

        regulation = card_data["regulation"]

        if regulation not in regulation_cards:
            regulation_cards[regulation] = []

        regulation_cards[regulation].append(
        (
            card_name,
            card_data["quantity"],
            card_data["set"]
        )
    )

    for regulation in sorted(regulation_cards):

        print(f"\n{regulation}")
        print("-" * len(regulation))

        for card_name, qty, set_name in sorted(
            regulation_cards[regulation]
        ):
            print(f"{card_name} ({set_name}): {qty}")

    print()

    for regulation, qty in sorted(regulation_counts.items()):
        print(f"{regulation}: {qty}")

    print()

    set_counts = {}

    for card_data in collection.values():

        set_name = card_data["set"]

        if set_name not in set_counts:
            set_counts[set_name] = 0

        set_counts[set_name] += card_data["quantity"]

    print("Set Breakdown")
    print("-------------")

    for set_name, qty in sorted(set_counts.items()):
        print(f"{set_name}: {qty}")

    print()

    results = []

    for filename in os.listdir("decks"):

        deck_path = os.path.join("decks", filename)

        if filename.endswith(".csv"):

            deck = load_deck_csv(deck_path)

        elif filename.endswith(".txt"):

            deck = load_limitless_deck(deck_path)

        else:
            continue

        completion, missing_cards = compare_deck(
            collection,
            deck
        )

        results.append({
            "deck": os.path.splitext(filename)[0],
            "completion": completion,
            "missing": missing_cards
        })

    results.sort(
        key=lambda x: x["completion"],
        reverse=True
    )

    best_deck = results[0]

    print("Best Deck Recommendation")
    print("------------------------")
    print(f"Deck: {best_deck['deck']}")
    print(f"Completion: {best_deck['completion']:.1f}%")
    print()

    print("Deck Rankings")
    print("----------------------------------")

    rank = 1

    for result in results:

        print(f"\n#{rank} - {result['deck']}")
        print(f"Completion: {result['completion']:.1f}%")

        if result["completion"] == 100:
            print("Status: BUILDABLE")
        elif result["completion"] >= 90:
            print("Status: VERY CLOSE")
        elif result["completion"] >= 75:
            print("Status: CLOSE")
        else:
            print("Status: NOT CLOSE")

        if result["missing"]:

            missing_card_types = len(result["missing"])
            missing_copies = sum(result["missing"].values())

            print(f"Missing Card Types: {missing_card_types}")
            print(f"Missing Copies: {missing_copies}")
            print()

            print("Missing Cards:")

            for card, qty in result["missing"].items():
                print(f"  - {card} x{qty}")

        else:
            print("Deck is buildable!")

        rank += 1

    all_missing = {}

    for result in results:

        for card, qty in result["missing"].items():

            if card not in all_missing:
                all_missing[card] = 0

            all_missing[card] += qty

    clear_wishlist()

    for card, qty in all_missing.items():

        add_wishlist_card(
            card,
            qty
        )

    print("\nMost Needed Cards")
    print("------------------")

    sorted_missing = sorted(
        all_missing.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for card, qty in sorted_missing[:10]:
        print(f"{card}: {qty}")

    print("\nCard Search")
    print("-----------")

    ...
    
    print("\nProgram Complete")