import random
import string


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


def validate_card(file_data: bytes) -> bool:
    """All of our Digicam Business Cards
        have the same first 41 bytes. We
        will use this as a way to block
        other files from being uploaded"""
    if file_data[0:41] == b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52\x00\x00\x08\x95\x00\x00\x05\x42\x08\x03\x00\x00\x00\x81\xBC\xAA\x08\x00\x00\x03\x00\x50\x4C\x54\x45':
        return True
