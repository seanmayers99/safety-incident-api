from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {
        "message": "Welcome to the Safety Incident API!",
        "available_endpoints": ["/register", "/login", "/incidents"]
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
