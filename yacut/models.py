import random
import re
from datetime import datetime

from flask import url_for

from settings import (
    MAX_LENGTH_SHORT_ID, LENGTH_SHORT_ID, APPROVED_SYMBOLS,
    REGEX_SYMBOLS_SHORT, NAME_FUNK_SHORT_ID, MAX_LENGTH_ORIGINAL_LINK
)
from yacut import db
from yacut.error_handlers import (
    EmploymentShortId, InvalidRegex, InvalidLength
)

INVALID_LENGTH_ORIGINAL = (
    f'Маскимальная длина ссылки {MAX_LENGTH_ORIGINAL_LINK} символов.'
)
INVALID_SHORT_ID = 'Указано недопустимое имя для короткой ссылки'
EMPLOYMENT_SHORT_ID = 'Имя "{short}" уже занято.'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LENGTH_ORIGINAL_LINK), nullable=False)
    short = db.Column(db.String(MAX_LENGTH_SHORT_ID), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self) -> dict:
        return dict(url=self.original,
                    short_link=URLMap.full_short_id(self.short))

    @staticmethod
    def get(short_id):
        return URLMap.query.filter_by(short=short_id).first()

    @staticmethod
    def get_uniq_short_id() -> str:
        uniq_short_id = ''
        uniq = False
        while not uniq:
            uniq_short_id = ''.join(random.choices(APPROVED_SYMBOLS,
                                                   k=LENGTH_SHORT_ID))
            if not URLMap.get(uniq_short_id):
                uniq = True
        return uniq_short_id

    @staticmethod
    def create_link(original_link: str, short_id: str):
        if len(original_link) > MAX_LENGTH_ORIGINAL_LINK:
            raise InvalidLength(INVALID_LENGTH_ORIGINAL)
        if short_id:
            if len(short_id) > MAX_LENGTH_SHORT_ID:
                raise InvalidLength(INVALID_SHORT_ID)
            if not re.search(REGEX_SYMBOLS_SHORT, short_id):
                raise InvalidRegex(INVALID_SHORT_ID)
        if not short_id or None:
            short_id = URLMap.get_uniq_short_id()
        if URLMap.get(short_id) is not None:
            raise EmploymentShortId(EMPLOYMENT_SHORT_ID.format(short=short_id))
        url_map = URLMap(original=original_link, short=short_id)
        db.session.add(url_map)
        db.session.commit()
        return url_map

    @staticmethod
    def full_short_id(short_id):
        return url_for(NAME_FUNK_SHORT_ID, short=short_id, _external=True)
