from flask import Flask, request, jsonify

app = Flask(__name__)

tipke = []

@app.route('/')
def index():
    return " ".join(tipke)


@app.route('/data', methods=['POST'])
def save_data():
    data = request.json
    keys = data.get('keys', [])
    tipke.extend(keys)
    print(f'Prejeto: {keys}')

    return jsonify({"status": "saved"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)