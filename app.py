from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask is running!"

# ✅ Route to receive location data
@app.route("/location", methods=["POST"])
def receive_location():
    try:
        data = request.get_json()
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if latitude is None or longitude is None:
            return jsonify({"error": "Missing latitude or longitude"}), 400

        print(f"📍 Received Location: Latitude={latitude}, Longitude={longitude}")

        return jsonify({"message": "Location received successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
