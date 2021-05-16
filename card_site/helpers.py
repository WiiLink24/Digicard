import random
import shutil
import string

from models import Orders


def save_card_data(order_id: str, discord_id: int):
    # Move card to assets
    original = rf"orders/{order_id}/Page\ 1.jpg"
    moved = rf"assets/cards/{discord_id}.jpg"
    shutil.move(original, moved)

def generate_random(length: int):
    """We use a simple random number generator
    in order to avoid Discord or a web
    browser from caching the photo"""
    letters = string.ascii_letters
    password = ''.join(random.choice(letters) for i in range(length))

    return password


def validate_card(card_id: int) -> bool:
    # Checks if the card exists in our database
    check_db = Orders.query.filter_by(order_id=card_id).first()
    print(check_db)

    # It cannot query a column if the order_id doesn't exist.
    # So we check for it's existence first.
    if check_db is None:
        return False

    # Now that we know the card exists, we can query the is_business_card column.
    if check_db.is_business_card == 1:
        print(check_db.is_business_card)
        return True

    if check_db.is_business_card == 0:
        print(check_db.is_business_card)
        return False