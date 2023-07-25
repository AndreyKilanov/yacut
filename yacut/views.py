from flask import render_template, flash, redirect, abort, url_for

from yacut import app
from yacut.constatns import MESSAGES, INDEX_HTML
from yacut.forms import URLForm
from yacut.models import URLMap
from yacut.utils import creating_link_in_db


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template(INDEX_HTML, form=form)
    custom_id = form.custom_id.data

    if URLMap.object_url(custom_id) is not None:
        flash(MESSAGES['bed_custom_id'].format(short=custom_id))
        return render_template(INDEX_HTML, form=form)

    url_map = creating_link_in_db(form.original_link.data, custom_id)
    short_link = url_for('get_url_map', short=url_map.short, _external=True)
    return render_template(INDEX_HTML, form=form, short_link=short_link)


@app.route('/<short>')
def get_url_map(short):
    url = URLMap.object_url(short)
    if url:
        return redirect(url.original, 302)
    abort(404)
