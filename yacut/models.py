import random
import re
from datetime import datetime

from flask import url_for

from settings import (
    MAX_LENGTH_ORIGINAL, MAX_LENGTH_CUSTOM, LENGTH_SHORT_ID, APPROVED_SYMBOLS,
    API_SYMBOLS_SHORT
)
from yacut import db
from yacut.error_handlers import InvalidAPIUsage

INVALID_SHORT_ID = 'Указано недопустимое имя для короткой ссылки'
CUSTOM_ID_EMPLOYMENT = 'Имя "{short}" уже занято.'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LENGTH_ORIGINAL), nullable=False)
    short = db.Column(db.String(MAX_LENGTH_CUSTOM), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self) -> dict:
        return dict(url=self.original,
                    short_link=URLMap.full_short_link(self.short))

    @staticmethod
    def get_url_map(short_link):
        return URLMap.query.filter_by(short=short_link).first()

    @staticmethod
    def get_short_id() -> str:
        return ''.join(random.choices(APPROVED_SYMBOLS, k=LENGTH_SHORT_ID))

    @staticmethod
    def create_link(original_link: str, custom_id: str):
        if URLMap.get_url_map(custom_id) is not None:
            raise InvalidAPIUsage(
                CUSTOM_ID_EMPLOYMENT.format(short=custom_id),
                400)
        if (custom_id and not re.search(API_SYMBOLS_SHORT, custom_id) or
                custom_id and len(custom_id) > MAX_LENGTH_CUSTOM):
            raise InvalidAPIUsage(INVALID_SHORT_ID, 400)
        if URLMap.get_url_map(custom_id):
            raise
        if not custom_id or None:
            custom_id = URLMap.get_short_id()
        url = URLMap(original=original_link, short=custom_id)
        db.session.add(url)
        db.session.commit()
        return url

    @staticmethod
    def full_short_link(short_link):
        return url_for('get_url_map', short=short_link, _external=True)
