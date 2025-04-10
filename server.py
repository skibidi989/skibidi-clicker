import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="public")

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('public', path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # используем порт, который задаёт Render
    app.run(host="0.0.0.0", port=port)
