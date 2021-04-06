import random
import string


def save_card_data(discord_id: int, card_data: bytes):
    # Move card to assets
    card = open(f"assets/cards/{discord_id}.png", "wb")
    card.write(card_data)
    card.close()


def generate_random(length: int):
    letters = string.ascii_letters
    password = ''.join(random.choice(letters) for i in range(length))

    return password
