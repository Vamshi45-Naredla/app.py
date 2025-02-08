from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Flask is running! Use /location to send location data."

@app.route("/location", methods=["POST"])
def log_location():
    try:
        data = request.json
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if latitude is None or longitude is None:
            return jsonify({"error": "❌ Missing latitude or longitude!"}), 400

        # ✅ Log location for debugging (Check Render Logs)
        print(f"📍 Received Location: Latitude={latitude}, Longitude={longitude}")

        return jsonify({"message": "✅ Location received!", "latitude": latitude, "longitude": longitude}), 200

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({"error": "❌ Internal server error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
