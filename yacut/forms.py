from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import (URL, Length, DataRequired,
                                Optional, ValidationError, regexp)

from settings import (REGEX_SYMBOLS_SHORT_ID, MAX_LENGTH_SHORT_ID,
                      MAX_LENGTH_ORIGINAL)
from yacut.models import URLMap

URL_FIELD = 'Введите ссылку'
URL_ERROR = 'Некорректная ссылка'
URL_SHORT_ID = 'Введите короткую ссылку'
URL_LENGTH = 'Превышена максимальная длина ссылки'
REQUIRED = 'Обязательное поле'
CREATE = 'Создать'
NAME_EMPLOYMENT = 'Имя {short} уже занято!'
INVALID_SHORT_ID = 'Указано недопустимое имя для короткой ссылки'


class URLForm(FlaskForm):
    original_link = URLField(
        URL_FIELD,
        validators=[
            DataRequired(REQUIRED),
            URL(require_tld=True, message=URL_ERROR),
            Length(max=MAX_LENGTH_ORIGINAL, message=URL_LENGTH)
        ]
    )
    custom_id = StringField(
        URL_SHORT_ID,
        validators=[
            Length(max=MAX_LENGTH_SHORT_ID, message=URL_LENGTH),
            regexp(REGEX_SYMBOLS_SHORT_ID, message=INVALID_SHORT_ID),
            Optional()
        ]
    )
    submit = SubmitField(CREATE)

    @staticmethod
    def validate_custom_id(original_link, short_id):
        if URLMap.get(short_id.data):
            raise ValidationError(NAME_EMPLOYMENT.format(short=short_id.data))
