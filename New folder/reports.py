from database import get_all_cards


def reports_menu():

    while True:

        print("\nReports")
        print("-------")
        print("1. Collection Summary")
        print("2. Regulation Breakdown")
        print("3. Set Breakdown")
        print("4. Back")

        choice = input("Choice: ")

        if choice == "1":
            collection_summary()

        elif choice == "2":
            regulation_breakdown()

        elif choice == "3":
            set_breakdown()

        elif choice == "4":
            break

        else:
            print("Invalid Choice")

def collection_summary():

    cards = get_all_cards()

    unique_cards = len(cards)

    total_cards = sum(
        card[1]
        for card in cards
    )

    print("\nCollection Summary")
    print("------------------")
    print(f"Unique Cards: {unique_cards}")
    print(f"Total Cards: {total_cards}")

def regulation_breakdown():

    cards = get_all_cards()

    regulations = {}

    for card in cards:

        regulation = card[2]
        quantity = card[1]

        regulations[regulation] = (
            regulations.get(
                regulation,
                0
            )
            + quantity
        )

    print("\nRegulation Breakdown")
    print("--------------------")

    for regulation, quantity in sorted(
        regulations.items()
    ):
        print(
            f"{regulation}: "
            f"{quantity}"
        )

def set_breakdown():

    cards = get_all_cards()

    sets = {}

    for card in cards:

        set_code = card[3]
        quantity = card[1]

        sets[set_code] = (
            sets.get(
                set_code,
                0
            )
            + quantity
        )

    print("\nSet Breakdown")
    print("-------------")

    for set_code, quantity in sorted(
        sets.items()
    ):
        print(
            f"{set_code}: "
            f"{quantity}"
        )