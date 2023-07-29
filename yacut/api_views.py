from flask import request, jsonify

from yacut import app
from yacut.error_handlers import InvalidURLMap
from yacut.models import URLMap

REQUEST_EMPTY = 'Отсутствует тело запроса'
MISSING_REQUIRED_FIELD_URL = '\"url\" является обязательным полем!'
MISSING_REQUIRED_FIELD_SHORT_ID = '\"custom_id\" является обязательным полем!'
INVALID_SHORT_ID = 'Указанный id не найден'


@app.route('/api/id/', methods=['POST'])
def create_new_short_link():
    data = request.get_json()
    if not data:
        raise InvalidURLMap(REQUEST_EMPTY)
    if 'url' not in data:
        raise InvalidURLMap(MISSING_REQUIRED_FIELD_URL)
    if 'custom_id' not in data and None:
        raise InvalidURLMap(MISSING_REQUIRED_FIELD_SHORT_ID)
    url_map = URLMap.create_link(data.get('url'), data.get('custom_id'))
    return jsonify(url_map.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_link(short_id):
    object_url_map = URLMap.get(short_id)
    if not object_url_map:
        raise InvalidURLMap(INVALID_SHORT_ID, 404)
    return jsonify(url=object_url_map.original), 200
