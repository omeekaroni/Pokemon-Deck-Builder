deck = {}

with open("dragapult.txt") as file:

    for line in file:

        line = line.strip()

        if not line:
            continue

        parts = line.split()

        quantity = int(parts[0])

        card_name = " ".join(parts[1:-2])

        deck[card_name] = quantity

print(deck)