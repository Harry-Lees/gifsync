import os
from flask import Flask, redirect, request, render_template, send_from_directory, url_for

app = Flask(__name__)


@app.before_request
def remove_trailing_slashes():
    request_path = request.path
    if request_path != '/' and request_path.endswith('/'):
        return redirect(request_path[:-1])


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/collection")
def collection():
    test_images = []
    for i in range(1, 14):
        test_images.append({
            'src': url_for('static', filename='img/image-placeholder.png'),
            'label': f'Image #{i}'
        })
    return render_template('collection.html', title='My Gifs', images=test_images)


@app.route('/create')
def create():
    return render_template('create.html', title='New Gif')


@app.route('/show')
def show():
    synced_image_src = url_for('static', filename='img/image-placeholder.png')
    return render_template('show.html', title='Synced Gif', synced_image=synced_image_src)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')
