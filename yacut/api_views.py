import re

from flask import request, jsonify

from yacut import app
from yacut.constatns import MESSAGES, MAX_LENGTH_SHORT_ID, API_SYMBOLS_SHORT
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.utils import creating_link_in_db


@app.route('/api/id/', methods=['POST'])
def create_new_short_link():
    data = request.get_json()

    if not data:
        raise InvalidAPIUsage(MESSAGES['request_empty'], 400)

    original_link = data.get('url')
    short_link = data.get('custom_id')

    if not original_link:
        raise InvalidAPIUsage(MESSAGES['missing_required_field'], 400)

    if URLMap.object_url(short_link) is not None:
        raise InvalidAPIUsage(
            MESSAGES['api_custom_id'].format(short=short_link), 400
        )

    if (short_link and not re.search(API_SYMBOLS_SHORT, short_link) or
            short_link and len(short_link) > MAX_LENGTH_SHORT_ID):
        raise InvalidAPIUsage(MESSAGES['invalid_short_id'], 400)

    url_map = creating_link_in_db(original_link, short_link)
    return jsonify(url_map.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_url(short_id):
    object_link = URLMap.object_url(short_id)

    if not object_link:
        raise InvalidAPIUsage(MESSAGES['invalid_id'], 404)

    return jsonify(url=object_link.original), 200
