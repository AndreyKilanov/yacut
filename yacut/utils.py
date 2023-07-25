import random

from yacut import db
from yacut.constatns import SYMBOLS, LENGTH_SHORT_ID
from yacut.models import URLMap


def get_unique_short_id() -> str:
    return ''.join(random.choices(SYMBOLS, k=LENGTH_SHORT_ID))


def creating_link_in_db(original_link: str, custom_id: str) -> URLMap:
    if not custom_id or None:
        custom_id = get_unique_short_id()
    url = URLMap(original=original_link, short=custom_id)
    db.session.add(url)
    db.session.commit()
    return url
