from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import URL, Length, DataRequired, Optional

from yacut.constatns import MESSAGES


class URLForm(FlaskForm):
    original_link = URLField(
        MESSAGES['url_field'],
        validators=[DataRequired(message=MESSAGES['required']),
                    URL(require_tld=True, message=MESSAGES['url_err'])]
    )
    custom_id = StringField(
        MESSAGES['custom_id'],
        validators=[Length(1, 16, message=MESSAGES['length']), Optional()]
    )
    submit = SubmitField(MESSAGES['create'])
