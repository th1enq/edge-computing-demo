from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/receive", methods=["POST"])
def receive_data():
    data = request.json
    print("🚀 Dữ liệu nhận từ Edge:", data)
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(debug=True)
