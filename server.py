from flask import Flask, send_from_directory, request, jsonify
import os, json

app = Flask(__name__)

ORDERS_FILE = os.path.join(os.getcwd(), "orders.json")

@app.route("/orders.json")
def get_orders():
    return send_from_directory(os.getcwd(), "orders.json")

@app.route("/")
def index():
    return send_from_directory(os.getcwd(), "index.html")

# ← 追加: Bot が叩く更新用API
@app.route("/update", methods=["POST"])
def update_orders():
    try:
        data = request.json
        with open(ORDERS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
