from .extensions import app, jsonify

@app.route('/')
def index():
    return jsonify(name = "Steve")