from app import app,env
from flask import render_template, send_from_directory, url_for
import os,sys



# Base directory for file exploration
BASE_DIR = os.path.abspath('../')

@app.route('/')
def index():
    items = os.listdir(BASE_DIR)
    links = [f"/view/{item}" for item in items]
    contents = list(zip(items, links))
    return render_template('index.html',contents=contents)

@app.route('/view/<path:subpath>')
def view(subpath):
    full_path = os.path.join(BASE_DIR, subpath)
    print(BASE_DIR,full_path)
    if os.path.isdir(full_path):
        items = os.listdir(full_path)
        links = [f"/view/{subpath}/{item}" for item in items]
        contents = list(zip(items, links))
        return render_template('directory.html', items=contents, subpath=subpath)
    else:
        file_extension = os.path.splitext(full_path)[1].lower()
        if file_extension in ['.png', '.jpg', '.jpeg', '.gif', '.mp4', '.webm']:
            return render_template('media.html', file=f"/serve/{subpath}", file_type=file_extension)
        else:
            return send_from_directory(os.path.dirname(full_path), os.path.basename(full_path), as_attachment=True)

@app.route('/serve/<path:subpath>')
def serve(subpath):
    full_path = os.path.join(BASE_DIR, subpath)
    return send_from_directory(os.path.dirname(full_path), os.path.basename(full_path))
