from database import get_wishlist


def wishlist_menu():

    print("WISHLIST FUNCTION CALLED")
    
    print("\nWishlist")
    print("--------")

    cards = get_wishlist()

    if not cards:

        print("Wishlist Empty")

    else:

        for card, qty in cards:

            print(f"{card}: {qty}")

    input(
        "\nPress Enter To Continue..."
    )