from flask import render_template

from yacut.forms import URLForm
from yacut.models import URLMap
from yacut import app, db


@app.route('/')
def index_view():
    url_form = URLForm
    return render_template('index.html', url_form=url_form)
