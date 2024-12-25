# protocols/http_protocol.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def fetch_data():
    # Mocked data source
    return jsonify({"data": {"cpu": 70, "memory": 50, "disk": 30}})

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json
    processed_data = {k: round(v, 2) for k, v in data.get("data", {}).items()}
    return jsonify({"processed_data": processed_data})

@app.route('/log', methods=['POST'])
def log_data():
    data = request.json
    print(f"Logged Data: {data}")
    return jsonify({"status": "success", "logged_data": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
