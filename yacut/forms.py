from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import URL, Length, DataRequired

messages = {
    'url_field': 'Введите ссылку',
    'url_err': 'Некорректный URL',
    'custom_id': 'Введите кастомный ID',
    'length': 'Длина не может быть меньше 1 и больше 16 символов',
    'required': 'Обязательное поле'
}


class URLForm(FlaskForm):
    original_link = URLField(
        messages['url_field'],
        validators=[DataRequired(message=messages['required']),
                    URL(require_tld=True, message=messages['url_err'])]
    )
    custom_id = StringField(
        messages['custom_id'],
        validators=[Length(1, 16, message=messages['length'])]
    )
    submit = SubmitField('Создать')
