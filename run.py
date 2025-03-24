from flask import Flask

app = Flask(__name__)

# 👇 Add this route just after the app is defined
@app.route("/")
def home():
    return {
        "message": "Welcome to the Safety Incident API!",
        "available_endpoints": ["/register", "/login", "/incidents"]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

