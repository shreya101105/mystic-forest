from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return """
    <h1>🏠 Mystic Forest IoT Server</h1>
    <p>Waiting for sensor data...</p>
    """

# POST API for ESP
@app.route("/post_data", methods=["POST"])
def post_data():
    data = request.get_json()
    print("📡 Sensor Data Received:", data)
    return {"status": "success"}, 200

if __name__ == "__main__":
    app.run()
