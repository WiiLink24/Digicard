import random
import string
import models

def save_card_data(discord_id: int, card_data: bytes):
    # Move card to assets
    card = open(f"assets/cards/{discord_id}.png", "wb")
    card.write(card_data)
    card.close()


def generate_random(length: int):
    """We use a simple random number generator
        in order to avoid Discord or a web
        browser from caching the photo"""
    letters = string.ascii_letters
    password = ''.join(random.choice(letters) for i in range(length))

    return password


def validate_card(card_id: int) -> bool:
    if models.Orders.query().filter_by(order_id=card_id).first().is_business_card:
        return True
