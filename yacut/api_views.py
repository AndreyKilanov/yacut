from flask import request, jsonify

from yacut import app
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap

REQUEST_EMPTY = 'Отсутствует тело запроса'
MISSING_REQUIRED_FIELD = '\"url\" является обязательным полем!'
INVALID_ID = 'Указанный id не найден'


@app.route('/api/id/', methods=['POST'])
def create_new_short_link():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(REQUEST_EMPTY, 400)
    if 'url' not in data:
        raise InvalidAPIUsage(MISSING_REQUIRED_FIELD, 400)
    url_map = URLMap.create_link(data.get('url'), data.get('custom_id'))
    return jsonify(url_map.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_url(short_id):
    object_link = URLMap.get_url_map(short_id)
    if not object_link:
        raise InvalidAPIUsage(INVALID_ID, 404)
    return jsonify(url=object_link.original), 200
