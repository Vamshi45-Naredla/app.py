from flask import Flask, request

app = Flask(__name__)

@app.route('/location', methods=['POST'])
def receive_location():
    data = request.json
    print(f"Received location: {data['latitude']}, {data['longitude']}")
    return {"status": "success"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
