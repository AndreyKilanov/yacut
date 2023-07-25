MESSAGES = {
    # messages for form
    'url_field': 'Введите ссылку',
    'url_err': 'Некорректный URL',
    'custom_id': 'Введите кастомный ID',
    'length': 'Длина не может быть меньше 1 и больше 16 символов',
    'required': 'Обязательное поле',
    'create': 'Создать',
    # messages for views
    'bed_custom_id': 'Имя {short} уже занято!',
    # messages for api_views
    'request_empty': 'Отсутствует тело запроса',
    'invalid_short_id': 'Указано недопустимое имя для короткой ссылки',
    'missing_required_field': '\"url\" является обязательным полем!',
    'invalid_id': 'Указанный id не найден',
    'api_custom_id': 'Имя "{short}" уже занято.',
}

# for generate short url
SYMBOLS = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'
LENGTH_SHORT_ID = 6

INDEX_HTML = 'yacut.html'

# for api symbols short
API_SYMBOLS_SHORT = '^[a-zA-Z0-9]+$'
MAX_LENGTH_SHORT_ID = 16
