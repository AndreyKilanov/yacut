import re

from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import (
    URL, Length, DataRequired, Optional, ValidationError
)

from settings import MAX_LENGTH_ORIGINAL, MAX_LENGTH_CUSTOM, API_SYMBOLS_SHORT
from yacut.models import URLMap


URL_FIELD = 'Введите ссылку'
URL_ERROR = 'Некорректный URL'
CUSTOM_ID = 'Введите кастомный ID'
LENGTH = 'Длина ссылки не может быть больше {symbols} символов'
REQUIRED = 'Обязательное поле'
CREATE = 'Создать'
NAME_EMPLOYMENT = 'Имя {short} уже занято!'
INVALID_SHORT_ID = 'Указано недопустимое имя для короткой ссылки'


class URLForm(FlaskForm):
    original_link = URLField(
        URL_FIELD,
        validators=[DataRequired(REQUIRED),
                    URL(require_tld=True, message=URL_ERROR),
                    Length(max=MAX_LENGTH_ORIGINAL,
                           message=LENGTH.format(symbols=MAX_LENGTH_ORIGINAL))]
    )
    custom_id = StringField(
        CUSTOM_ID,
        validators=[Length(
            max=MAX_LENGTH_CUSTOM,
            message=LENGTH.format(symbols=MAX_LENGTH_CUSTOM)
        ), Optional()]
    )
    submit = SubmitField(CREATE)

    @staticmethod
    def validate_custom_id(original, short):
        if URLMap.get_url_map(short.data):
            raise ValidationError(NAME_EMPLOYMENT.format(short=short.data))
        if not re.search(API_SYMBOLS_SHORT, short.data):
            raise ValidationError(INVALID_SHORT_ID)
