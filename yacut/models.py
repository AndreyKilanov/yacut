from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self) -> dict:
        short_link = url_for('get_url_map', short=self.short, _external=True)
        return dict(url=self.original, short_link=short_link)

    @staticmethod
    def object_url(short_link):
        return URLMap.query.filter_by(short=short_link).first()
