from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Base directory for file exploration
BASE_DIR = os.path.join(os.getcwd(),'D:/')

@app.route('/')
def index():
    """List all directories and files in the base directory."""
    items = os.listdir(BASE_DIR)
    return render_template('index.html', items=items)

@app.route('/view/<path:subpath>')
def view_directory(subpath):
    """Handle directory and file rendering."""
    full_path = os.path.join(BASE_DIR, subpath)
    if os.path.isdir(full_path):
        # List contents if it's a directory
        items = os.listdir(full_path)
        return render_template('directory.html', items=items, subpath=subpath)
    else:
        # Render multimedia or trigger download
        file_extension = os.path.splitext(full_path)[1].lower()
        if file_extension in ['.mkv','.png', '.jpg', '.jpeg', '.gif', '.mp4', '.webm']:
            return render_template('media.html', file=subpath, file_type=file_extension)
        else:
            return send_from_directory(os.path.dirname(full_path), os.path.basename(full_path), as_attachment=True)

@app.route('/<path:filename>')
def serve_file(filename):
    """Serve files directly using the absolute path."""
    full_path = os.path.join(BASE_DIR, filename)
    directory = os.path.dirname(full_path)
    file_name = os.path.basename(full_path)
    return send_from_directory(directory, file_name)

if __name__ == '__main__':
    app.run(host='192.168.0.101',port=2000)


