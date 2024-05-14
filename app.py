from flask import Flask, request, json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/api', methods=['GET', 'POST'])
def api():
    rec = request.get_json()
    print(rec)
    return json.jsonify(rec)


if __name__ == '__main__':
    app.run()
