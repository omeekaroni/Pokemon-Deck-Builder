from collection_manager import run_collection_manager
from app import run_deck_analyzer
from reports import reports_menu
from wishlist import wishlist_menu 

while True:

    print("1. Collection Manager")
    print("2. Deck Analyzer")
    print("3. Reports")
    print("4. Wishlist")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        run_collection_manager()

    elif choice == "2":
        run_deck_analyzer()

    elif choice == "3":
        reports_menu()

    elif choice == "4":
        wishlist_menu()

    elif choice == "5":
        break

    else:
        print("Invalid Choice")