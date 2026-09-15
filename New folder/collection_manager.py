from database import (
    get_all_cards,
    get_card,
    add_card,
    update_quantity,
    delete_card,
    get_cards_by_regulation,
    get_cards_by_set
)


def show_menu():
    print("\nCollection Manager")
    print("------------------")
    print("1. View Collection")
    print("2. Search Card")
    print("3. Add Card")
    print("4. Update Quantity")
    print("5. Delete Card")
    print("6. View Cards By Regulation")
    print("7. View Cards By Set")
    print("8. Exit")

def view_collection():

    cards = get_all_cards()

    for card in cards:
        print(card)

def search_card():

    search = input("Card Name: ")

    card = get_card(search)

    if card:
        print(card)
    else:
        print("Card not found.")

def add_card_menu():

    card_name = input("Card Name: ")

    quantity = int(
        input("Quantity: ")
    )

    regulation = input(
        "Regulation: "
    ).upper()

    set_code = input(
        "Set Code: "
    ).upper()

    add_card(
        card_name,
        quantity,
        regulation,
        set_code
    )

    print("Card Added")

def update_quantity_menu():

    card_name = input("Card Name: ")

    quantity = int(
        input("New Quantity: ")
    )

    rows = update_quantity(
        card_name,
        quantity
    )

    if rows == 0:
        print("Card not found.")
    else:
        print("Quantity Updated")

def delete_card_menu():

    card_name = input(
        "Card Name To Delete: "
    )

    rows = delete_card(card_name)

    if rows == 0:
        print("Card not found.")
    else:
        print("Card Deleted")

def view_by_regulation():

    regulation = input(
        "Enter Regulation: "
    ).upper()

    cards = get_cards_by_regulation(
        regulation
    )

    if not cards:

        print("No cards found.")

    else:

        print(
            f"\nCards In Regulation {regulation}"
        )

        print("------------------------")

        for card in cards:

            print(
                f"{card[0]} "
                f"({card[2]}): "
                f"{card[1]}"
            )

def view_by_set():

    set_code = input(
        "Enter Set Code: "
    ).upper()

    cards = get_cards_by_set(
        set_code
    )

    if not cards:

        print("No cards found.")

    else:

        print(
            f"\nCards In Set {set_code}"
        )

        print("--------------------")

        for card in cards:

            print(
                f"{card[0]} "
                f"(Regulation {card[2]}): "
                f"{card[1]}"
            )
    
def run_collection_manager():

    while True:

        show_menu()

        choice = input("Choice: ")

        if choice == "1":
            view_collection()

        elif choice == "2":
            search_card()

        elif choice == "3":
            add_card_menu()

        elif choice == "4":
            update_quantity_menu()

        elif choice == "5":
            delete_card_menu()

        elif choice == "6":
            view_by_regulation()

        elif choice == "7":
            view_by_set()

        elif choice == "8":
            break

        else:
            print("Invalid Choice")